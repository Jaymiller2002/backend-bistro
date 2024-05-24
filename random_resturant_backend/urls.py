"""
URL configuration for random_resturant_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from random_resturant_backend_app.views import ProductViewSet, MenuItemViewSet, ReservationViewSet, SignInViewSet, SignUpViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'sign-ins', SignInViewSet)
router.register(r'sign-ups', SignUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

