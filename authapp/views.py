from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "authapp/login.html"


class LogoutView(TemplateView):
    pass


class RegisterView(TemplateView):
    pass


class EditView(TemplateView):
    pass
