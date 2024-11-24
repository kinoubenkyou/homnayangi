from pathlib import Path

from homnayangi.settings_base import *  # noqa: F403
from homnayangi.settings_base import DATABASES

ALLOWED_HOSTS = []

DATABASES["default"]["HOST"] = "postgres"

with Path("postgres_password").open() as file:
    DATABASES["default"]["PASSWORD"] = file.read()

DEBUG = True

with Path("django_secret_key").open() as f:
    SECRET_KEY = f.read().strip()
