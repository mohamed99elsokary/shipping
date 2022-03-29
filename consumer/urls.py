from django.urls import path
from . import views

urlpatterns = [
    path("company-register", views.company_register),
    path("consumer-register", views.consumer_register),
    path("login", views.login),
    path("company-orders", views.company_orders),
    path("consumer-orders", views.consumer_orders),
    path("order", views.order),
]
