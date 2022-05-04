# Generated by Django 3.1.4 on 2022-05-04 06:56

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220503_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 12, 26, 14, 128588)),
        ),
    ]
