document.addEventListener('DOMContentLoaded', () => {
    initForm();
});

const STATE = {
    form: document.getElementById('paymentForm'),
    loading: document.getElementById('paymentLoading'),
    ready: document.getElementById('paymentReady'),
    error: document.getElementById('paymentError')
};

function showState(name) {
    Object.values(STATE).forEach(el => { if (el) el.style.display = 'none'; });
    if (STATE[name]) STATE[name].style.display = 'block';
}

/* ---------- Form + CPF mask ---------- */
function initForm() {
    const form = document.getElementById('customerForm');
    const cpfInput = document.getElementById('inputCpf');

    if (cpfInput) {
        cpfInput.addEventListener('input', (e) => {
            let v = e.target.value.replace(/\D/g, '');
            if (v.length > 11) v = v.slice(0, 11);
            if (v.length > 9) v = v.replace(/(\d{3})(\d{3})(\d{3})(\d+)/, '$1.$2.$3-$4');
            else if (v.length > 6) v = v.replace(/(\d{3})(\d{3})(\d+)/, '$1.$2.$3');
            else if (v.length > 3) v = v.replace(/(\d{3})(\d+)/, '$1.$2');
            e.target.value = v;
        });
    }

    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const nome = document.getElementById('inputNome').value.trim();
            const email = document.getElementById('inputEmail').value.trim();
            const cpf = document.getElementById('inputCpf').value.trim();

            if (!nome || !email || !cpf) return;
            createPayment(nome, email, cpf);
        });
    }
}

/* ---------- Create Payment ---------- */
async function createPayment(nome, email, cpf) {
    showState('loading');

    try {
        const response = await fetch('/api/create-payment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, email, cpf })
        });

        if (!response.ok) {
            const err = await response.json().catch(() => ({}));
            throw new Error(err.error || 'Erro ao criar pagamento');
        }

        const data = await response.json();
        displayPayment(data);
        startPolling(data.token);
        startTimer();
    } catch (error) {
        console.error('Payment error:', error);
        showState('error');
    }
}

/* ---------- Display QR Code ---------- */
function displayPayment(data) {
    const qrImg = document.getElementById('qrCodeImg');
    const pixCode = document.getElementById('pixCode');

    if (qrImg && data.qr_code_image) {
        qrImg.src = 'data:image/png;base64,' + data.qr_code_image;
    }

    if (pixCode && data.qr_code_text) {
        pixCode.value = data.qr_code_text;
    }

    showState('ready');
    initCopyButton();
}

/* ---------- Copy PIX Code ---------- */
function initCopyButton() {
    const copyBtn = document.getElementById('copyBtn');
    const pixCode = document.getElementById('pixCode');
    const feedback = document.getElementById('copyFeedback');

    if (!copyBtn || !pixCode) return;

    copyBtn.addEventListener('click', async () => {
        try {
            await navigator.clipboard.writeText(pixCode.value);
        } catch {
            pixCode.select();
            document.execCommand('copy');
        }

        if (feedback) {
            feedback.style.opacity = '1';
            setTimeout(() => { feedback.style.opacity = '0'; }, 2000);
        }

        copyBtn.classList.add('copied');
        setTimeout(() => copyBtn.classList.remove('copied'), 2000);
    });
}

/* ---------- Poll Payment Status ---------- */
function startPolling(token) {
    let attempts = 0;
    const maxAttempts = 200;

    const interval = setInterval(async () => {
        attempts++;

        if (attempts >= maxAttempts) {
            clearInterval(interval);
            const statusEl = document.getElementById('paymentStatus');
            if (statusEl) {
                statusEl.innerHTML =
                    '<div class="status-indicator">' +
                    '<div class="status-dot expired"></div>' +
                    '<span>Tempo expirado. Recarregue a página.</span>' +
                    '</div>';
            }
            return;
        }

        try {
            const response = await fetch('/api/check-payment/' + token);
            if (!response.ok) return;

            const data = await response.json();

            if (data.paid) {
                clearInterval(interval);
                showPaymentConfirmed();
                setTimeout(() => {
                    window.location.href = '/sucesso';
                }, 2000);
            }
        } catch {
            // Retry silently
        }
    }, 3000);
}

/* ---------- Payment Confirmed ---------- */
function showPaymentConfirmed() {
    const paymentCard = STATE.ready?.closest('.checkout-card');
    if (!paymentCard) return;

    paymentCard.innerHTML =
        '<div class="payment-confirmed">' +
        '<div class="confirmed-icon">' +
        '<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2">' +
        '<circle cx="12" cy="12" r="10"/>' +
        '<path d="M8 12l3 3 5-5"/>' +
        '</svg>' +
        '</div>' +
        '<h2>Pagamento confirmado!</h2>' +
        '<p>Redirecionando para o download...</p>' +
        '<div class="loading-bar"><div class="loading-bar-fill"></div></div>' +
        '</div>';
}

/* ---------- Timer ---------- */
function startTimer() {
    const timerEl = document.getElementById('timerCount');
    if (!timerEl) return;

    let minutes = 30;
    let seconds = 0;

    const interval = setInterval(() => {
        if (seconds === 0) {
            if (minutes === 0) {
                clearInterval(interval);
                timerEl.textContent = 'Expirado';
                return;
            }
            minutes--;
            seconds = 59;
        } else {
            seconds--;
        }

        timerEl.textContent =
            String(minutes).padStart(2, '0') + ':' +
            String(seconds).padStart(2, '0');
    }, 1000);
}

/* ---------- Retry Button ---------- */
document.getElementById('retryBtn')?.addEventListener('click', () => {
    showState('form');
});
