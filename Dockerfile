FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


CMD ["streamlit", "run", "app.py", "--server.address", "127.0.0.1", "--server.port", "8080"]

