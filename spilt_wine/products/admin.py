from django.contrib import admin
from .models import Product, Appellation, Region, WineType, Brand, CountryState, Varietal, Style, Body

# Register your models here.
admin.site.register(Appellation)
admin.site.register(Region)
admin.site.register(WineType)
admin.site.register(Brand)
admin.site.register(CountryState)
admin.site.register(Varietal)
admin.site.register(Style)
admin.site.register(Body)
admin.site.register(Product)