from rest_framework.serializers import ModelSerializer

from app.restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Restaurant