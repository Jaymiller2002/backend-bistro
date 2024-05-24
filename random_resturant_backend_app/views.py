from rest_framework import viewsets
from .models import Product, Reservation, SignIn, SignUp, MenuItem
from .serializer import ProductSerializer, ReservationSerializer, SignInSerializer, SignUpSerializer, MenuItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class SignInViewSet(viewsets.ModelViewSet):
    queryset = SignIn.objects.all()
    serializer_class = SignInSerializer

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

