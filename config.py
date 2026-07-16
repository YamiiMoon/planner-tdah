import os
from dotenv import load_dotenv

load_dotenv()

# --- Produto ---
PRODUCT_NAME = os.getenv("PRODUCT_NAME", "Planner TDAH Produtivo")
PRODUCT_DESCRIPTION = os.getenv("PRODUCT_DESCRIPTION", "Sistema de organização projetado para o cérebro TDAH")
PRODUCT_PRICE = float(os.getenv("PRODUCT_PRICE", "29.90"))

# --- Asaas ---
ASAAS_API_KEY = os.getenv("ASAAS_API_KEY", "")
ASAAS_ENVIRONMENT = os.getenv("ASAAS_ENVIRONMENT", "sandbox")
ASAAS_WEBHOOK_TOKEN = os.getenv("ASAAS_WEBHOOK_TOKEN", "")

ASAAS_URLS = {
    "sandbox": "https://sandbox.asaas.com/api/v3",
    "production": "https://api.asaas.com/v3"
}

# --- Arquivo PDF ---
PDF_FILENAME = os.getenv("PDF_FILENAME", "planner-tdah-produtivo.pdf")

# --- Visual ---
PRIMARY_COLOR = "#4F46E5"
BRAND_NAME = "CATreport"

# --- Contato ---
INSTAGRAM = os.getenv("INSTAGRAM", "@catreport")
EMAIL = os.getenv("EMAIL", "contato@catreport.com")
WHATSAPP = os.getenv("WHATSAPP", "")

# --- SEO ---
SITE_TITLE = "Planner TDAH Produtivo | CATreport"
SITE_DESCRIPTION = "Sistema de organização projetado especificamente para o cérebro TDAH. 120 páginas de ferramentas práticas, flexíveis e sem julgamento."
SITE_URL = os.getenv("SITE_URL", "https://seudominio.com")

# --- Servidor ---
SECRET_KEY = os.getenv("SECRET_KEY", "troque-esta-chave-em-producao")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))
