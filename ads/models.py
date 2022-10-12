from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class ADS(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    is_published = models.CharField(max_length=1000)
