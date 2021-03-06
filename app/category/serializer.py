from rest_framework.serializers import ModelSerializer

from app.category.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category