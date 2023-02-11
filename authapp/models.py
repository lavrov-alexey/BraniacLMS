from django.contrib.auth.models import AbstractUser
from django.db import models

from mainapp.models import NULLABLE


# наследуемся от встроенного абстрактного (в "Мета" у него поле abstract=True, т.е. от него ничего лишнего не торчит
# в потомках) пользователя и переопределяем нужные нам поля и методы
class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name="Email", unique=True)
    age = models.PositiveSmallIntegerField(**NULLABLE, verbose_name="Age")
    avatar = models.ImageField(upload_to="users", **NULLABLE, verbose_name="Avatar")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
