from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products = ["Cherries", "Apples", "Oranges", "strawberries", "Pears", "Watermelons"]
    context = {
        #keyword :
        'products': products,
    }
    return render(request, "home.html", context)
