# Generated by Django 3.1.4 on 2022-05-19 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220519_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('can_add_new_blog', 'Can add a new Blog'), ('can_change_blog', 'can change this blog')]},
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 18, 48, 39, 137903)),
        ),
    ]
