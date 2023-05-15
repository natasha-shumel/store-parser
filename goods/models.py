from django.db import models
from selections.models import Selections


class Goods(models.Model):
    selection_id = models.ForeignKey(Selections, on_delete=models.CASCADE)
    name = models.CharField("Наименование товара", max_length=10000, null=True)
    price = models.CharField("Цена", max_length=10000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "goods"

