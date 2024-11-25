from pathlib import Path

from django.core.management.utils import get_random_secret_key

with Path("django_secret_key").open("w") as file:
    file.write(get_random_secret_key())
