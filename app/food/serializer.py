from rest_framework.serializers import ModelSerializer

from app.food.models import Food


class FoodSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Food
