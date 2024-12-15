from os import environ

from homnayangi.settings_base import *  # noqa: F403

ALLOWED_HOSTS = environ["DJANGO_ALLOWED_HOSTS"].split(",")

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
