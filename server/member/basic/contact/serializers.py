import re
from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.RegexField(r'^\d{0,10}$', allow_blank=True)
    mobile = serializers.RegexField(r'^\d{0,10}$', allow_blank=True)

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        return instance
