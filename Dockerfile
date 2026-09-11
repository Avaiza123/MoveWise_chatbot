FROM python:3.11-slim

WORKDIR /app

COPY backend_chatbot/requirements.txt /app/backend_chatbot/requirements.txt
RUN pip install --no-cache-dir -r /app/backend_chatbot/requirements.txt

COPY backend_chatbot /app/backend_chatbot

WORKDIR /app/backend_chatbot

ENV PORT=8000
ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} app.main:app"]
