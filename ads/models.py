from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ADS(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='logos/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    items = models.ManyToManyField(ADS)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name