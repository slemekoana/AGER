from rest_framework import serializers
from .models import Product, productType, provider, Cart, CartItem

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'type', 'provider', 'image')

class productTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = productType
        fields = ('name', 'description')

class providerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = provider
        fields = ('name', 'info')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    model = Cart
    fields = ('user', 'created_at', 'checked_out')

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    model = CartItem
    fields = ('product', 'quantity', 'price', 'cart')