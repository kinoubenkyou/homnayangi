from os import environ

from homnayangi.settings import *


ALLOWED_HOSTS = environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")

DATABASES["default"]["HOST"] = environ.get("POSTGRES_HOST")

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
    },
}
