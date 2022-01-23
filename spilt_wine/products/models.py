from django.db import models


# model Classes are in order of proper database ingestion
class Appellation(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # class methods borrowed from Code Institute
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Region(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    # attrib setting from Code Institute, if a value is deleted in this table set value to NULL in other tables
    appellation = models.ForeignKey('Appellation', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WineType(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CountryState(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    region = models.ForeignKey('Region', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Varietal(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    wine_type = models.ForeignKey('WineType', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    img_file_name = models.ImageField(null=True, blank=True)
    vintage = models.IntegerField(null=True, blank=True)
    size = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey('Brand', null=True, blank=True)
    country_state = models.ForeignKey('CountryState')
    region = models.ForeignKey('Region', null=True, blank=True)
    appellation = models.ForeignKey('Appellation', null=True, blank=True)
    wine_type = models.ForeignKey('WineType')
    varietal = models.ForeignKey('Varietal')
    style = models.CharField(max_length=25, null=True, blank=True)
    abv = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    taste = models.TextField(max_length=100, null=True, blank=True)
    body = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name