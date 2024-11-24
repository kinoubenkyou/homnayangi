from os import environ

from homnayangi.settings_base import *  # noqa: F403
from homnayangi.settings_base import DATABASES

ALLOWED_HOSTS = environ["DJANGO_ALLOWED_HOSTS"].split(",")

DATABASES["default"]["HOST"] = environ["POSTGRES_HOST"]
DATABASES["default"]["PASSWORD"] = environ["POSTGRES_PASSWORD"]

DEBUG = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "ERROR",
    },
}

SECRET_KEY = environ["DJANGO_SECRET_KEY"]
