from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.ReadOnlyField()  # id del owner (read-only)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'type',
            'talle',
            'is_active',
            'created_at',
            'slug',
            'main_image',
            'owner',
            'owner_username',
        ]
        read_only_fields = ['id', 'created_at', 'slug', 'owner', 'owner_username']