# Generated by Django 3.1.4 on 2022-05-19 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220519_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('can_add_new_blog', 'Can add a new Blog')]},
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 17, 10, 25, 356353)),
        ),
    ]
