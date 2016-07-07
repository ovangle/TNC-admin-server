from rest_framework import serializers

from .availability_hours import AvailableHoursField

class AvailabilitySerializer(serializers.Serializer):
    mon = AvailableHoursField(source='mon_hours', allow_null=True)
    tue = AvailableHoursField(source='tue_hours', allow_null=True)
    wed = AvailableHoursField(source='wed_hours', allow_null=True)
    thu = AvailableHoursField(source='thu_hours', allow_null=True)
    fri = AvailableHoursField(source='fri_hours', allow_null=True)