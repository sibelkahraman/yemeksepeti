from django.conf.urls import url

from app.ingredient.views import IngredientView

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'post': 'create', 'get': 'list'}


urlpatterns = [
    url(r'/(?P<pk>\d+)/', IngredientView.as_view(detailed), name='category_detail'),
    url(r'', IngredientView.as_view(general), name='category')
]
