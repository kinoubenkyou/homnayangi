FROM python:3.13.0
WORKDIR /app
RUN apt update -y
RUN apt install -y chromium chromium-driver
COPY requirements.txt .
RUN pip install -r requirements.txt
