# Generated by Django 4.2.1 on 2023-05-23 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2023, 5, 23, 19, 27, 57, 366617, tzinfo=datetime.timezone.utc)),
        ),
    ]