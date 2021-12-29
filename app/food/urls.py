from django.conf.urls import url

from app.food.views import FoodView

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'post': 'create', 'get': 'list'}

urlpatterns = [
    url(r'/(?P<pk>\d+)/', FoodView.as_view(detailed), name='food_detail'),
    url(r'', FoodView.as_view(general), name='food')
]
