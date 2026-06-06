FROM python:3.12-alpine

WORKDIR /app

COPY server.py .
COPY index.html .

EXPOSE 5000

CMD ["python", "server.py"]
