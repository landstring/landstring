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

class Teams(models.Model):
    name = models.CharField(verbose_name="Название команды", max_length=500)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "команда"
        verbose_name_plural = "Команды"
    
class User_Team(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Teams, 
        on_delete=models.CASCADE,
    )
    Roles = (
        (1, "Создатель"),
        (2, "Ведущий программист"),
        (3, "Креативный директор"),
        (4, "Главный менеджер"),
        (5, "Программист"),
        (6, "Менеджер"),
    )
    role = models.CharField(max_length=100,
                            choices=Roles,
    )

    def __str__(self) -> str:
        return (self.user + ' ' + self.team + ' ' + self.role)

    class Meta:
        verbose_name = "участник"
        verbose_name_plural = "Участники"
    
class Application(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Teams, 
        on_delete=models.CASCADE,
    )
    Roles = (
        (1, "Ведущий программист"),
        (2, "Креативный директор"),
        (3, "Главный менеджер"),
        (4, "Программист"),
        (5, "Менеджер"),
    )
    role = models.CharField(max_length=2,
                            choices=Roles,
    )

    def __str__(self) -> str:
        return (self.user.username + ' ' + self.team.name + ' ' + self.role)

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "Заявки"

class Invitation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Teams, 
        on_delete=models.CASCADE,
    )
    Roles = (
        (1, "Ведущий программист"),
        (2, "Креативный директор"),
        (3, "Главный менеджер"),
        (4, "Программист"),
        (5, "Менеджер"),
    )
    role = models.CharField(max_length=2,
                            choices=Roles,
    )

    def __str__(self) -> str:
        return (self.user + ' ' + self.team + ' ' + self.role)

    class Meta:
        verbose_name = "приглашение"
        verbose_name_plural = "Приглашения"

class TeamProject(models.Model):
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
        verbose_name = "командный проект"
        verbose_name_plural = "Командные проекты"

class Stage_of_TeamProject(models.Model):
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
        verbose_name = "этап командного проекта"
        verbose_name_plural = "Этапы командных проектов"

class Task_of_TeamProject(models.Model):
    name = models.CharField(verbose_name="Задача", max_length=500)
    stage = models.ForeignKey(
        Stage_of_PersonalProject, 
        on_delete=models.CASCADE,
        )
    completed = models.BooleanField(verbose_name="Задача выполнена")

    def __str__(self) -> str:
        return (str(self.stage) + "  --->  " + self.name)

    class Meta:
        verbose_name = "задача командного проекта на текущем этапе"
        verbose_name_plural = "Задачи командных проекта на текущем этапе"