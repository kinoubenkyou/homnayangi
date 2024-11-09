from django.views.generic import TemplateView


class UserSignedInView(TemplateView):
    template_name = "user/signed_in.html"
