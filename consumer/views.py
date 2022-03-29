from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models
from company import serializers as company_serializers, models as company_models
from django.contrib.auth import authenticate


@api_view(["POST"])
def company_register(request):
    serializer = serializers.CompanyRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def consumer_register(request):
    serializer = serializers.ConsumerRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login(request):
    serializer = serializers.LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        if serializer.consumer:
            serializer = serializers.ConsumerSerializer(serializer.consumer)
            data = serializer.data
            data["type"] = "consumer"
        elif serializer.company:
            serializer = company_serializers.CompanySerializer(serializer.company)
            data = serializer.data
            data["type"] = "company"

    return Response(data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def company_orders(request):
    company_id = request.data.get("company")
    orders = models.Order.objects.filter(company_id=company_id)
    serializer = serializers.OrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def consumer_orders(request):
    consumer_id = request.data.get("consumer")
    orders = models.Order.objects.filter(consumer_id=consumer_id)
    serializer = serializers.OrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def order(request):
    serializer = serializers.OrdersSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
