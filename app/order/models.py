from django.db import models

from app.user.models import User
from app.food.models import Food
from app.restaurant.models import Restaurant

ORDER_STATUS = [
    (0, 'waiting'),
    (1, 'released'),
]


class Order(models.Model):
    food = models.ManyToManyField(Food)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=ORDER_STATUS, default='waiting', max_length=10)
    restaurant = models.ForeignKey(Restaurant, blank=False, on_delete=models.CASCADE, default=1)


