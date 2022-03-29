from django.db import models
from django.contrib.auth.models import User

services_types = (
    ("sea freight", "sea freight"),
    ("land_shipping", "land shipping"),
    ("custom clearance", "custom clearance"),
)


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Company(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    logo = models.ImageField(
        upload_to="media/", height_field=None, width_field=None, max_length=None
    )
    is_sea_freight = models.BooleanField()
    is_land_shipping = models.BooleanField()
    is_customs_clearance = models.BooleanField()

    def __str__(self):
        return self.name


class Pricing(models.Model):
    # relations
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_pricing"
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    # fields
    service = models.CharField(max_length=50, choices=services_types)
    price = models.IntegerField()

    def __str__(self):
        return self.company.name
