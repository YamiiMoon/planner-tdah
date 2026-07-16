FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p secure static/img

EXPOSE 10000

CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120"]
