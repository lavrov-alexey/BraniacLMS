# Create your models here.
from django.db import models

# в целях оптимизации - создадим "константный" словарь для передачи в полях параметров возможности пустых
NULLABLE = {"blank": True, "null": True}


# Базовая модель с общими полями и методами для всех моделей
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    deleted = models.BooleanField(default=False, verbose_name="Удален")

    # переопределяем удаление на "мягкое" удаление - в виде изменения статуса, без реального удаления данных
    def __del__(self):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True  # чтобы в БД не создавались лишние взаимосвязи базы с ост. таблицами (моделями)
        # с "-" обратная сортировка (как DESC), без него - прямая (как ASC). Список/кортеж
        ordering = [
            "-created_at",
        ]


class News(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Title")
    preambule = models.CharField(max_length=1024, verbose_name="Preambule")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
