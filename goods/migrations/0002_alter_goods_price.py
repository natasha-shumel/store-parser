# Generated by Django 4.2 on 2023-05-13 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
    ]