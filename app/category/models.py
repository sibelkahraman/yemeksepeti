from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=25)