from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from .residential_stability import ResidentialStability
from .residence_type import ResidenceType
from .models import ResidentialStatus


class ResidentialStatusSerializer(serializers.Serializer):
    type = EnumField(enum_type=ResidenceType)
    stability = EnumField(enum_type=ResidentialStability)

    def create(self, validated_data):
        return ResidentialStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.stability = validated_data.get('stability', instance.stability)
        return instance

