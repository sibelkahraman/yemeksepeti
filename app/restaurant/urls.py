from django.conf.urls import url

from app.restaurant.views import RestaurantView

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'post': 'create', 'get': 'list'}


urlpatterns = [
    url(r'/(?P<pk>\d+)/', RestaurantView.as_view(detailed), name='category_detail'),
    url(r'', RestaurantView.as_view(general), name='category')
]
