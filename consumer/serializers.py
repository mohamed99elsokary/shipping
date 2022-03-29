from company import models as company_models
from company import serializers as company_serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class CompanyRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = company_models.Company
        exclude = ("user",)
        extra_kwargs = {
            "user": {"validators": []},
            "logo": {"read_only": True},
        }

    def validate(self, data):
        user = User.objects.filter(username=data["username"])
        if user:
            raise serializers.ValidationError({"error": "username is taken already"})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(username=validated_data["username"])
        user.set_password(password)
        user.save()
        company = company_models.Company.objects.create(
            name=validated_data["name"],
            user=user,
            is_customs_clearance=validated_data["is_customs_clearance"],
            is_land_shipping=validated_data["is_land_shipping"],
            is_sea_freight=validated_data["is_sea_freight"],
        )
        return company


class ConsumerRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.Consumer
        exclude = ("user",)

    def validate(self, data):
        user = User.objects.filter(username=data["username"])
        if user:
            raise serializers.ValidationError({"error": "username is taken already"})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(username=validated_data["username"])
        user.set_password(password)
        user.save()
        consumer = models.Consumer.objects.create(
            user=user,
            name=validated_data["name"],
        )
        return consumer


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consumer
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            self.consumer = None
            self.company = None
            try:
                consumer = models.Consumer.objects.get(user=user)
                self.consumer = consumer
            except:
                company = company_models.Company.objects.get(user=user)
                self.company = company
        else:

            raise serializers.ValidationError(
                {"error": "Invalid Username And Password"}
            )
        return data


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
