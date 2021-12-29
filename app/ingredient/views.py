from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.ingredient.models import Ingredient
from app.ingredient.serializer import IngredientSerializer


class IngredientView(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IngredientSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Ingredient.objects.filter(pk=instance.pk).delete()
        return Response(status=204)

