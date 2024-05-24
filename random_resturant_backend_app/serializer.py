from rest_framework import serializers
from .models import Product, MenuItem, Reservation, SignIn, SignUp

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'category', 'description', 'price']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'name', 'email', 'date', 'time', 'party_size', 'special_request']

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = ['id', 'username', 'password']

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ['id', 'username', 'password', 'email']