from django.db import models

from app.ingredient.models import Ingredient
from app.category.models import Category


class Food(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ManyToManyField(Category)

