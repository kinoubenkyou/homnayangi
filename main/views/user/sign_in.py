from django.contrib.auth.views import LoginView


class UserSignInView(LoginView):
    template_name = "user/sign_in.html"
