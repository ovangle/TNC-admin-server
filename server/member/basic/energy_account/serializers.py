from rest_framework import serializers

from ext.rest_framework.fields import EnumField
from .energy_retailer import EnergyRetailer
from .models import EnergyAccount

class EnergyAccountSerializer(serializers.Serializer):
    retailer = EnumField(enum_type=EnergyRetailer, allow_null=True)
    account_number = serializers.CharField(max_length=32, allow_blank=True)

    def create(self, validated_data):
        return EnergyAccount.objects.create(**validated_data)