from rest_framework.serializers import ModelSerializer

from app.ingredient.models import Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ingredient
