from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.category.serializer import CategorySerializer
from app.category.models import Category


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorySerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Category.objects.filter(pk=instance.pk).delete()
        return Response(status=204)
