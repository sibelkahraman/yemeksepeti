from django.conf.urls import url

from app.category.views import CategoryView

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'post': 'create', 'get': 'list'}


urlpatterns = [
    url(r'/(?P<pk>\d+)/', CategoryView.as_view(detailed), name='category_detail'),
    url(r'', CategoryView.as_view(general), name='category')
]
