from django.conf.urls import url

from app.user.views import UserView

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'post': 'create', 'get': 'list'}


urlpatterns = [
    url(r'/(?P<pk>\d+)/', UserView.as_view(detailed), name='user_detail'),
    url(r'', UserView.as_view(general), name='user')
]

