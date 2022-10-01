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
        }

    def validate(self, data):
        if user := User.objects.filter(username=data["username"]):
            raise serializers.ValidationError({"error": "username is taken already"})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(username=validated_data["username"])
        user.set_password(password)
        user.save()
        validated_data.pop("username")
        return company_models.Company.objects.create(user=user, **validated_data)


class ConsumerRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.Consumer
        exclude = ("user",)

    def validate(self, data):
        if user := User.objects.filter(username=data["username"]):
            raise serializers.ValidationError({"error": "username is taken already"})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(username=validated_data["username"])
        user.set_password(password)
        user.save()
        password = validated_data.pop("username")
        return models.Consumer.objects.create(user=user, **validated_data)


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consumer
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if user := authenticate(
            username=data["username"], password=data["password"]
        ):
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
