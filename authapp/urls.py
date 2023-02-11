from django.urls import path

from authapp.apps import AuthappConfig
from authapp.views import EditView, LoginView, LogoutView, RegisterView

app_name = AuthappConfig

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("login/", LogoutView.as_view(), name="logout"),
    path("login/", RegisterView.as_view(), name="register"),
    path("login/", EditView.as_view(), name="edit"),
]
