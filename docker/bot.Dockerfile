FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot /app/bot
COPY config.py /app/

CMD ["python", "-m", "bot"]