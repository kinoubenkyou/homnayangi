FROM python:3.13.0
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=homnayangi.settings_production
