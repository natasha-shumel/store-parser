# Generated by Django 4.2 on 2023-05-13 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 5, 13, 23, 25, 57, 355439), verbose_name='Время')),
                ('quantity', models.IntegerField(null=True, verbose_name='Число товаров')),
            ],
            options={
                'verbose_name': 'Отбор',
                'verbose_name_plural': 'Отборы',
                'db_table': 'selections',
            },
        ),
    ]
