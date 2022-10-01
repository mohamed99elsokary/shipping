from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from . import serializers, models
from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(["GET"])
def materials(request):
    materials = models.Material.objects.all()
    serializer = serializers.MaterialsSerializer(materials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def companies_for_(request):
    service = request.data.get("service")
    material = request.data.get("material")
    weight = request.data.get("weight")

    companies = models.Pricing.objects.filter(service=service, material_id=material)
    serializer = serializers.CompanyPricingSerializer(companies, many=True)
    data = serializer.data
    for company in data:
        company["price"] = int(company["price"]) * int(weight)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT"])
def company(request, id):
    company = get_object_or_404(models.Company, id=id)
    if request.method == "GET":
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        company.delete()
        return Response(status=status.HTTP_200_OK)

    elif request.method == "PUT":
        name = request.data.get("name")
        is_land_shipping = request.data.get("is_land_shipping")
        is_sea_freight = request.data.get("is_sea_freight")
        is_customs_clearance = request.data.get("is_customs_clearance")
        if name not in [None, ""]:
            company.name = name
        if is_land_shipping not in [None, ""]:
            company.is_land_shipping = is_land_shipping
        if is_sea_freight not in [None, ""]:
            company.is_sea_freight = is_sea_freight
        if is_customs_clearance not in [None, ""]:
            company.is_customs_clearance = is_customs_clearance
        company.save()
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", "DELETE", "PUT", "GET"])
def company_pricing(request, id=None):
    if request.method == "POST":
        serializer = serializers.CompanyPricingSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "GET":
        prices = models.Pricing.objects.filter(company_id=id)
        serializer = serializers.CompanyPricingSerializer(prices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        id = request.data.get("id")
        price = request.data.get("price")
        pricing = models.Pricing.objects.get(id=id)
        if price is not None and price != "":
            pricing.price = price
        pricing.save()

        serializer = serializers.CompanyPricingSerializer(pricing)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        pricing = models.Pricing.objects.get(id=id)
        pricing.delete()
        return Response(status=status.HTTP_200_OK)
