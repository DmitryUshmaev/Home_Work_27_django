from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=20, decimal_places=10)
    lng = models.DecimalField(max_digits=20, decimal_places=10)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = ((MEMBER, 'Пользователь'),
               (ADMIN, 'Администратор'),
               (MODERATOR, 'Модератор'))


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=200, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=200, null=True)
    username = models.CharField(verbose_name='Логин', max_length=200, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=200)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=15)
    age = models.PositiveIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
