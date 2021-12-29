from django.conf.urls import url

from app.order.views import OrderView, CompleteOrderView, OrderView_by_Status

detailed = {'delete': 'destroy', 'patch': 'partial_update',
            'get': 'retrieve'}
general = {'get': 'list', 'post': 'create'}


urlpatterns = [
    url(r'/(?P<pk>\d+)/', OrderView.as_view(detailed), name='order_detail'),
    url(r'/complete/', CompleteOrderView.as_view({'get': 'update'}), name='complete_order'),
    url(r'/(?P<status>[\w-]+)/', OrderView_by_Status.as_view({'get': 'list'}), name='order_detail_by_status'),
    url(r'', OrderView.as_view(general), name='orders')
]
