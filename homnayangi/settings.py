from homnayangi.settings_base import *


ALLOWED_HOSTS = []

DATABASES["default"]["HOST"] = "postgres"

with Path("postgres_password").open() as file:
    DATABASES["default"]["PASSWORD"] = file.read()

DEBUG = True

with open("django_secret_key") as f:
    SECRET_KEY = f.read().strip()
