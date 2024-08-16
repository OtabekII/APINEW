from rest_framework.serializers import ModelSerializer
from Goods.models import Product, Category
from django.contrib.auth.models import User
from rest_framework import serializers

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ['image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user