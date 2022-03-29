from django.urls import path
from . import views

urlpatterns = [
    path("company/<int:id>", views.company),
    path("companies", views.companies_for_),
    path("materils", views.materials),
    path("company-prices/<int:id>", views.company_pricing),
]
