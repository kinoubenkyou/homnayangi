from django.contrib.admin import ModelAdmin, site
from django.contrib.auth.admin import UserAdmin

from main.models import Place, User


class PlaceAdmin(ModelAdmin):
    pass


site.register(User, UserAdmin)
site.register(Place, PlaceAdmin)
