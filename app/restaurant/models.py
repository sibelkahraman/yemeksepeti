from django.db import models

from app.food.models import Food


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(unique=True, blank=False, max_length=11)
    email = models.EmailField(unique=True, blank=True)
    foods = models.ManyToManyField(Food, blank=True, null=True)
