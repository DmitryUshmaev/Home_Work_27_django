# Generated by Django 4.0.1 on 2022-10-18 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.locations')),
            ],
        ),
    ]
