# Create your models here.
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    preamble = models.CharField(max_length=1000, verbose_name="Описание")
    body = models.TextField(verbose_name="Содержимое")
    body_as_markdown = models.BooleanField(default=False, verbose_name="Формат markdown")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    deleted = models.BooleanField(default=False, verbose_name="Удален")

    def __str__(self):
        return f"#{self.pk} {self.title}"

    def __del__(self):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = [
            "-created_at",
        ]  # с "-" обратная сортировка (как DESC), без него - прямая (как ASC). Список/кортеж
