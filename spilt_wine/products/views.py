from django.shortcuts import render
from .models import Wine


def all_products(request):
    """ Shows all products and handles sorting and searching. """

    wines = Wine.objects.all()

    wine_content = {
        'wines': wines,
    }

    return render(request, 'products/products.html', wine_content)


def all_wines(request):
    """ Shows all products and handles sorting and searching. """

    wines = Wine.objects.all()

    wine_content = {
        'wines': wines,
    }

    return render(request, 'products/wines.html', wine_content)
