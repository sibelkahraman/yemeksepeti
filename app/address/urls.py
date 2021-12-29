from django.conf.urls import url

from app.address.views import AddressView

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'post': 'create', 'get': 'list'}

urlpatterns = [
    url(r'/(?P<pk>\d+)/', AddressView.as_view(detailed), name='address_detail'),
    url(r'', AddressView.as_view(general), name='address')
]
