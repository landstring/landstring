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

class PersonalProject(models.Model):
    name = models.CharField(verbose_name="Название проекта", max_length=100)
    description = models.TextField(verbose_name="Описание проекта")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    completed = models.BooleanField(verbose_name="Проект выполнен")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "личный проект"
        verbose_name_plural = "Личные проекты"

class Stage_of_PersonalProject(models.Model):
    name = models.CharField(verbose_name="Название этапа", max_length=100)
    description = models.TextField(verbose_name="Описание этапа")
    project = models.ForeignKey(
        PersonalProject, 
        on_delete=models.CASCADE,
        )
    completed = models.BooleanField(verbose_name="Этап выполнен")
    
    def __str__(self) -> str:
        return (self.project.name + "  --->  " + self.name)

    class Meta:
        verbose_name = "этап личного проекта"
        verbose_name_plural = "Этапы личных проектов"


class Task_of_PersonalProject(models.Model):
    name = models.CharField(verbose_name="Задача", max_length=500)
    stage = models.ForeignKey(
        Stage_of_PersonalProject, 
        on_delete=models.CASCADE,
        )
    completed = models.BooleanField(verbose_name="Задача выполнена")

    def __str__(self) -> str:
        return (str(self.stage) + "  --->  " + self.name)

    class Meta:
        verbose_name = "задача личного проекта на текущем этапе"
        verbose_name_plural = "Задачи личного проекта на текущем этапе"