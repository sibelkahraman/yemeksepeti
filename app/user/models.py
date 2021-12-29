from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(unique=True, blank=False, max_length=11)
