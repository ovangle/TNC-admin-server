from django.db import models

from ext.django.fields import EnumField

from .proof_of_low_income import ProofOfLowIncome
from .benefit_type import BenefitType
from .income_type import IncomeType


class Income(models.Model):
    kind = 'member.basic::Income'

    type = EnumField(enum_type=IncomeType)
    proof_of_low_income = EnumField(enum_type=ProofOfLowIncome)

    benefit_type = EnumField(enum_type=BenefitType)
    # Should only be a non-empty value if benefit_type is OTHER, so allow 
    # null values (rather than just blank)
    benefit_other_description = models.CharField(max_length=32, null=True)
