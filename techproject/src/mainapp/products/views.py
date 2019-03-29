from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def admin.console(request):
    products =  Product.objects.all()
    return render(request, 'products/product_page.html', {'products':products})