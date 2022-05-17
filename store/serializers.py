from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['category', 'id', 'name', 'price', 'description', 'status', 'owner', 'image', 'created_at']