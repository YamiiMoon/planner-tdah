import os
import time
import uuid
import hmac
import hashlib
import requests
from flask import (
    Flask, render_template, jsonify, send_file,
    abort, session, redirect, url_for, request
)
from config import (
    ASAAS_API_KEY, ASAAS_ENVIRONMENT, ASAAS_URLS,
    PRODUCT_NAME, PRODUCT_DESCRIPTION, PRODUCT_PRICE,
    PDF_FILENAME, SECRET_KEY, DEBUG, HOST, PORT, ASAAS_WEBHOOK_TOKEN
)

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

ASAAS_TIMEOUT = 15
payments_db = {}


def get_asaas_url():
    return ASAAS_URLS.get(ASAAS_ENVIRONMENT, ASAAS_URLS["sandbox"])


def asaas_headers():
    return {
        "access_token": ASAAS_API_KEY,
        "Content-Type": "application/json"
    }


def cleanup_expired_payments():
    now = time.time()
    expired = [
        token for token, info in payments_db.items()
        if now - info["created_at"] > 3600
    ]
    for token in expired:
        del payments_db[token]


def create_asaas_customer(nome, email, cpf):
    url = f"{get_asaas_url()}/customers"
    payload = {
        "name": nome,
        "cpfCnpj": cpf,
        "email": email
    }
    try:
        response = requests.post(
            url, json=payload, headers=asaas_headers(), timeout=ASAAS_TIMEOUT
        )
        response.raise_for_status()
        return response.json().get("id")
    except requests.exceptions.Timeout:
        app.logger.error("Asaas timeout ao criar cliente")
        return None
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Asaas erro ao criar cliente: {e}")
        return None


def create_pix_charge(customer_id):
    url = f"{get_asaas_url()}/payments"
    payload = {
        "customer": customer_id,
        "billingType": "PIX",
        "value": PRODUCT_PRICE,
        "description": PRODUCT_NAME,
        "dueDate": time.strftime("%Y-%m-%d"),
        "externalReference": str(uuid.uuid4())
    }
    try:
        response = requests.post(
            url, json=payload, headers=asaas_headers(), timeout=ASAAS_TIMEOUT
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        app.logger.error("Asaas timeout ao criar cobrança")
        return None
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Asaas erro ao criar cobrança: {e}")
        return None


def get_pix_qr_code(payment_id):
    url = f"{get_asaas_url()}/payments/{payment_id}/pixQrCode"
    try:
        response = requests.get(
            url, headers=asaas_headers(), timeout=ASAAS_TIMEOUT
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        app.logger.error("Asaas timeout ao gerar QR Code")
        return None
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Asaas erro ao gerar QR Code: {e}")
        return None


def check_payment_status(payment_id):
    url = f"{get_asaas_url()}/payments/{payment_id}"
    try:
        response = requests.get(
            url, headers=asaas_headers(), timeout=ASAAS_TIMEOUT
        )
        response.raise_for_status()
        return response.json().get("status")
    except requests.exceptions.RequestException:
        return None


# --- Rotas públicas ---

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/sucesso")
def success():
    if not session.get("download_authorized"):
        return redirect(url_for("index"))
    return render_template("sucesso.html")


# --- API ---

@app.route("/api/create-payment", methods=["POST"])
def api_create_payment():
    cleanup_expired_payments()

    data = request.get_json(silent=True) or {}
    nome = data.get("nome", "").strip()
    email = data.get("email", "").strip()
    cpf = data.get("cpf", "").strip().replace(".", "").replace("-", "")

    if not nome or not email or not cpf:
        return jsonify({"error": "Preencha todos os campos."}), 400

    customer_id = create_asaas_customer(nome, email, cpf)
    if not customer_id:
        return jsonify({
            "error": "Serviço de pagamento temporariamente indisponível. Tente novamente em alguns segundos."
        }), 503

    payment = create_pix_charge(customer_id)
    if not payment:
        return jsonify({
            "error": "Não foi possível gerar a cobrança. Tente novamente."
        }), 503

    payment_id = payment["id"]

    qr_data = get_pix_qr_code(payment_id)
    if not qr_data:
        return jsonify({
            "error": "Não foi possível gerar o QR Code. Tente novamente."
        }), 503

    token = str(uuid.uuid4())
    payments_db[token] = {
        "payment_id": payment_id,
        "status": "PENDING",
        "created_at": time.time()
    }

    return jsonify({
        "payment_id": payment_id,
        "qr_code_image": qr_data.get("encodedImage", ""),
        "qr_code_text": qr_data.get("payload", ""),
        "token": token
    })


@app.route("/api/check-payment/<token>")
def api_check_payment(token):
    if token not in payments_db:
        return jsonify({"status": "NOT_FOUND"}), 404

    payment_info = payments_db[token]
    payment_id = payment_info["payment_id"]

    if payment_info["status"] in ("RECEIVED", "CONFIRMED", "RECEIVED_IN_CASH"):
        session["download_authorized"] = True
        session["download_token"] = token
        return jsonify({"status": payment_info["status"], "paid": True})

    status = check_payment_status(payment_id)
    if status:
        payments_db[token]["status"] = status

    paid = status in ("RECEIVED", "CONFIRMED", "RECEIVED_IN_CASH")

    if paid:
        session["download_authorized"] = True
        session["download_token"] = token

    return jsonify({
        "status": status or "UNKNOWN",
        "paid": paid
    })


# --- Download seguro ---

@app.route("/download")
def download():
    if not session.get("download_authorized"):
        abort(403)

    secure_dir = os.path.join(app.root_path, "secure")
    pdf_path = os.path.join(secure_dir, PDF_FILENAME)

    session.pop("download_authorized", None)
    session.pop("download_token", None)

    if not os.path.exists(pdf_path):
        abort(404)

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=PDF_FILENAME,
        mimetype="application/pdf"
    )


# --- Webhook Asaas ---

@app.route("/webhook/asaas", methods=["POST"])
def webhook_asaas():
    if ASAAS_WEBHOOK_TOKEN:
        incoming_token = request.headers.get("asaas-access-token", "")
        if not hmac.compare_digest(incoming_token, ASAAS_WEBHOOK_TOKEN):
            abort(401)

    data = request.json
    if not data:
        return jsonify({"received": True}), 200

    event = data.get("event", "")
    payment_data = data.get("payment", {})
    payment_id = payment_data.get("id")

    if event in ("PAYMENT_RECEIVED", "PAYMENT_CONFIRMED") and payment_id:
        for token, info in payments_db.items():
            if info["payment_id"] == payment_id:
                payments_db[token]["status"] = "RECEIVED"
                break

    return jsonify({"received": True}), 200


# --- Bloquear acesso direto ao PDF ---

@app.route("/secure/<path:filename>")
def block_secure(filename):
    abort(403)


# --- Erros ---

@app.errorhandler(403)
def forbidden(e):
    return render_template("index.html"), 403


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("index"))


if __name__ == "__main__":
    os.makedirs(os.path.join(app.root_path, "secure"), exist_ok=True)
    os.makedirs(os.path.join(app.root_path, "static", "img"), exist_ok=True)
    app.run(debug=DEBUG, host=HOST, port=PORT)
