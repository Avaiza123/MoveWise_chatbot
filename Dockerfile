FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

COPY backend_chatbot/requirements.txt /app/backend_chatbot/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/backend_chatbot/requirements.txt

COPY backend_chatbot /app/backend_chatbot

WORKDIR /app/backend_chatbot

EXPOSE 8000

CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT:-8000} fastapi_app:app"]
