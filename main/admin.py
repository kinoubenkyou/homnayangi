from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin

from main.models import User

site.register(User, UserAdmin)
