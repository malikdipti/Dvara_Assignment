from rest_framework import serializers
from app1.models import CatagoryModel,SubcatagoryModel

class CatagorySerializers(serializers.ModelSerializer):
    class Meta:
        model=CatagoryModel
        fields="__all__"

class SubcatagorySerializers(serializers.ModelSerializer):
    class Meta:
        model=SubcatagoryModel
        fields="__all__"