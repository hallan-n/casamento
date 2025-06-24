FROM python:3.12-slim

ENV TZ=America/Sao_Paulo

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]