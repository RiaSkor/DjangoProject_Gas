from django.db import models
from django.utils import timezone

class Chapter(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название главы")
    content = models.TextField(verbose_name="Содержание главы")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"
        ordering = ['created_at']

    def __str__(self):
        return self.title
