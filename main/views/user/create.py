from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms.user import UserCreateForm


class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("user-read")
    template_name = "form.html"
