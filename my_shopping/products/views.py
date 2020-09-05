from django.http import HttpResponse, request, HttpResponseRedirect
from rest_framework import viewsets

from products.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


def index(request):
    return HttpResponse("to get the product details! Enter the valid details..")


def products(request):
    product_list = Product.objects.all()
    product_dict = {'products': product_list}
    return render(request, 'products.html', context=product_dict)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm


def my_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/products')
        else:
            return render(request, 'my_form.html', {'form': form})
    else:
        form = MyForm()

    return render(request, 'my_form.html', {'form': form})