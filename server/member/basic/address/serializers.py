import re
from rest_framework import serializers

from .models import Address

_POSTCODE_REGEX = re.compile(r'^\d{4}$')

class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=256, allow_blank=True, required=False)
    city = serializers.CharField(max_length=32, allow_blank=True, required=False)
    postcode = serializers.CharField(max_length=4, allow_blank=True, required=False)

    def validate_postcode(self, value):
        if value != '' and not _POSTCODE_REGEX.match(value):
            raise serializers.ValidationError(
                'An Austrlaian postcode must be a string of 4 digits'
            )
        return value


    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.postcode = validated_data.get('postcode', instance.postcode)
        return instance

