# Generated by Django 4.0.1 on 2022-10-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_remove_user_location_id_alter_ads_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='category_id',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='ads',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]