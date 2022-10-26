from django.contrib import admin

from ads.models import Category, ADS

admin.site.register(ADS)
admin.site.register(Category)