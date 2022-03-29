from django.db import models
from django.contrib.auth.models import User
from company import models as company_models


class Consumer(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # fields
    name = models.CharField(max_length=50)
    profile_image = models.ImageField(
        upload_to="media/",
        height_field=None,
        width_field=None,
        max_length=None,
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    # relations
    company = models.ForeignKey(company_models.Company, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    from_country = models.CharField(max_length=50)
    to_country = models.CharField(max_length=50)
    weight = models.IntegerField()
    service = models.CharField(max_length=50, choices=company_models.services_types)
