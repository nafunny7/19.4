from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=50)  # имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # цена
    # размер файлов игры
    size = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()  # описание
    # ограничение возраста 18+
    age_limited = models.BooleanField(default=False)
    # покупатель, обладающий игрой
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title