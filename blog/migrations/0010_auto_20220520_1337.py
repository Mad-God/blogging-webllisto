# Generated by Django 3.1.4 on 2022-05-20 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220519_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('can_change_blog', 'can change this blog')]},
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 13, 37, 28, 655860)),
        ),
    ]
