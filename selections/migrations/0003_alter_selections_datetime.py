# Generated by Django 4.2 on 2023-05-13 23:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0002_alter_selections_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selections',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 13, 23, 33, 7, 884987), verbose_name='Время'),
        ),
    ]
