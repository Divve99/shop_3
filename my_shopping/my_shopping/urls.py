"""my_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from products import views
from products.views import my_form, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'router-products', ProductViewSet)
router.register(r'router-categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('my-form/', my_form, name='my_form'),
    path('', include(router.urls)),
    path('rest-api/', include('rest_framework.urls', namespace='rest_framework')),
]
