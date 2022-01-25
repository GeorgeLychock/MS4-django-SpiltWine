from django.shortcuts import render
from .models import Wine

# Create your views here.
def all_wines(request):
    """ Shows all products and handles sorting and searching. """

    wines = Wine.objects.all()

    wine_content = {
        'wines': wines,
    }

    return render(request, 'products/products.html', wine_content)