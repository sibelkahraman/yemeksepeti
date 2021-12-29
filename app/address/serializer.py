
from rest_framework.serializers import ModelSerializer

from app.address.models import Address


class AddressSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Address
