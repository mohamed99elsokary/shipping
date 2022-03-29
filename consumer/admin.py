from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Consumer)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class Admin(admin.ModelAdmin):
    pass
