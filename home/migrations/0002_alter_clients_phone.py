# Generated by Django 4.2.1 on 2023-05-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.IntegerField(max_length=12),
        ),
    ]