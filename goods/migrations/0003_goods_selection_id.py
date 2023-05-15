# Generated by Django 4.2 on 2023-05-13 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0004_alter_selections_datetime'),
        ('goods', '0002_alter_goods_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='selection_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='selections.selections'),
            preserve_default=False,
        ),
    ]
