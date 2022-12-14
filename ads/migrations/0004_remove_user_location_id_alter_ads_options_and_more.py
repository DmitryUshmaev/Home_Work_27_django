# Generated by Django 4.0.1 on 2022-10-24 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('ads', '0003_remove_ads_address_remove_ads_author_ads_author_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
        migrations.AlterModelOptions(
            name='ads',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='ads',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='users.user', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='ads',
            name='name',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
