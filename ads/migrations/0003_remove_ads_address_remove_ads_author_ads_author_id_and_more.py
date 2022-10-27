# Generated by Django 4.0.1 on 2022-10-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_locations_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='author',
        ),
        migrations.AddField(
            model_name='ads',
            name='author_id',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='category_id',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='image',
            field=models.ImageField(null=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='is_published',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='lat',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='lng',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.locations'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]