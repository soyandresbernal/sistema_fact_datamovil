# Generated by Django 2.1.2 on 2018-10-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='creado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]