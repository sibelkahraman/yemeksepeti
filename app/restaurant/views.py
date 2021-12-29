from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.restaurant.models import Restaurant
from app.restaurant.serializer import RestaurantSerializer


class RestaurantView(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RestaurantSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Restaurant.objects.filter(pk=instance.pk).delete()
        return Response(status=204)

