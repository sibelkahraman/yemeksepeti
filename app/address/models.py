from django.db import models

from app.user.models import User
from app.restaurant.models import Restaurant

ADDRESS_TYPE = [
    ('h', 'home'),
    ('r', 'restaurant'),
]


class Address(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    building_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(choices=ADDRESS_TYPE, default=None, max_length=10)
