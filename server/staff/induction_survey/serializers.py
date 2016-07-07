from rest_framework import serializers


class StaffInductionSurveySerializer(serializers.Serializer):
    has_previous_experience = serializers.BooleanField()

    skills = serializers.ListField(
        child=serializers.CharField(max_length=32)
    )
    traits = serializers.ListField(
        child=serializers.CharField(max_length=32)
    ) 

    date_available_to_start = serializers.DateField()
    desired_hours_per_week = serializers.IntegerField()
    referred_by = serializers.CharField(max_length=64)
    has_understood_privacy_obligations = serializers.BooleanField()