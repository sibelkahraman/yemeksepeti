from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from app.address.serializer import AddressSerializer
from app.address.models import Address


class AddressView(ModelViewSet):
    serializer_class = AddressSerializer
    lookup_field = 'pk'
    queryset = Address.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AddressSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Address.objects.filter(pk=instance.pk).delete()
        return Response(status=204)

