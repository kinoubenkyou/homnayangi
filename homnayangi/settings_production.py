from os import environ

from homnayangi.settings import *


ALLOWED_HOSTS = environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")

DATABASES["default"]["HOST"] = environ.get("POSTGRES_HOST")

DEBUG = False
