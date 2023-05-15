from django.db import models
from datetime import datetime


class Selections(models.Model):
    datetime = models.DateTimeField("Время", default=datetime.now())
    quantity = models.IntegerField("Число товаров", null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Отбор"
        verbose_name_plural = "Отборы"
        db_table = "selections"

