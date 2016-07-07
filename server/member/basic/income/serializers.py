from rest_framework import serializers

from ext.rest_framework.fields import EnumField

from .proof_of_low_income import ProofOfLowIncome
from .income_type import IncomeType
from .benefit_type import BenefitType

from .models import Income

class IncomeSerializer(serializers.Serializer):
    type = EnumField(enum_type=IncomeType)
    proof_of_low_income = EnumField(enum_type=ProofOfLowIncome)

    benefit_type = EnumField(enum_type=BenefitType)
    benefit_other_description = serializers.CharField(max_length=32, allow_blank=True, required=False)

    def validate(self, data):
        benefit_type = data.get('benefit_type')
        other_description = data.get('benefit_other_description')
        if (benefit_type != BenefitType.other 
            and other_description is not None):
            raise ValidationError(
                'Other description should not be provided unless '
                'benefit type is OTHER'
            )
        return data

    def create(self, validated_data):
        return Income.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.proof_of_low_income = validated_data.get('proof_of_low_income', instance.proof_of_low_income)
        instance.benefit_type = validated_data.get('benefit_type', instance.benefit_type)
        benefit_other_description = validated_data.get('benefit_type', instance.benefit_type)

        return instance



