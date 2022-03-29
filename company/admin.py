from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Company)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Material)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Pricing)
class Admin(admin.ModelAdmin):
    pass
