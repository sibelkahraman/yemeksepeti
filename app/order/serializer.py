from rest_framework.serializers import ModelSerializer

from app.order.models import Order


class OrderSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Order
