from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey

class Ideas(models.Model):
    name = models.CharField(verbose_name="Наименование идеи", max_length=100)
    description = models.TextField(verbose_name="Описание идеи")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "идею"
        verbose_name_plural = "Идеи"
    
class Comments(models.Model):
    comment = models.TextField(verbose_name="Текст комментария")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    idea = models.ForeignKey(
        Ideas, 
        on_delete=models.CASCADE,
        )
    def __str__(self) -> str:
        return (self.author.username + "  --->  " + self.idea.name)
    
    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "Комментарии"
