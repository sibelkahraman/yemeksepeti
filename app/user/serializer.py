from rest_framework.serializers import ModelSerializer

from app.user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User