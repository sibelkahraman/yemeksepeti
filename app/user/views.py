from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.user.models import User
from app.user.serializer import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        User.objects.filter(pk=instance.pk).delete()
        return Response(status=204)
