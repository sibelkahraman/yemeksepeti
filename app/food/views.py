from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.food.serializer import FoodSerializer
from app.food.models import Food


class FoodView(ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FoodSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Food.objects.filter(pk=instance.pk).delete()
        return Response(status=204)


