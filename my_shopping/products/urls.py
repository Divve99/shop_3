from django.urls import path, include
from rest_framework import routers

from products import views
from products.views import my_form, ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('products/my-form/', my_form, name='my_form'),
    path('', include(router.urls)),
    path('rest-api/', include('rest_framework.urls', namespace='rest_framework')),
    ]