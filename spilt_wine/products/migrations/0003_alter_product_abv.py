# Generated by Django 3.2 on 2022-01-24 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_body_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]