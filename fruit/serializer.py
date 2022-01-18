from rest_framework.serializers import ModelSerializer
from .models import Fruit
from region.serializer import RegionSerializer

class FruitSerializer(ModelSerializer):
    region = RegionSerializer

    class Meta:
        model = Fruit
        fields = '__all__'