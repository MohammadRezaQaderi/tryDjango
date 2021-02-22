from django.shortcuts import render
from .models import Product
# Create your views here.
def product_detail_view(request):
    # products = Product.objects.all()
    obj = Product.objects.get(id = 1)
    context = {
        'titel' : obj.titel,
        'description': obj.description 
    }
    # return render(request , "products/product_detail.html" , {'products' : products})
    return render(request , "products/product_detail.html" , context)