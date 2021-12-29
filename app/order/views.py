from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from app.order.models import Order
from app.order.serializer import OrderSerializer
from service.pub import Pub
from service.sub import Sub


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    service = Pub()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)

        self.service.create_order(instance.pk)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Order.objects.filter(pk=instance.pk).delete()
        return Response(status=204)


class OrderView_by_Status(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']
    lookup_field = 'status'

    def list(self, request, *args, **kwargs):
        status = kwargs.get('status')
        instance = self.queryset.filter(status=status)
        serializer = OrderSerializer(instance, many=True)
        return Response(serializer.data)


class CompleteOrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    http_method_names = ['get']
    service = Sub()

    def update(self, request, *args, **kwargs):
        order_ids = self.service.consumer()
        if order_ids:
            Order.objects.filter(pk__in=order_ids).update(status='released')
        return Response(status=status.HTTP_200_OK)
