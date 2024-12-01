from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from main.models import Place


class PlacesReadView(LoginRequiredMixin, DetailView):
    model = Place
    template_name = "places/read.html"
