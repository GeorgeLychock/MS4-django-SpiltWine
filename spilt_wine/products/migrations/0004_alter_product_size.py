# Generated by Django 3.2 on 2022-01-24 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_abv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
