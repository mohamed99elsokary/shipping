from rest_framework import serializers
from . import models


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        exclude = ("user",)


class CompanyPricingSerializer(serializers.ModelSerializer):
    company_details = CompanySerializer(read_only=True, source="company")

    material_name = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="name", source="material"
    )

    class Meta:
        model = models.Pricing
        fields = "__all__"
