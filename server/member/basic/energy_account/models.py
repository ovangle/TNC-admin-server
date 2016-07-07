from django.db import models
from ext.django.fields import EnumField

from .energy_retailer import EnergyRetailer

class EnergyAccount(models.Model):
    kind = 'member.basic::EnergyAccount'

    retailer = EnumField(enum_type=EnergyRetailer, null=True)
    account_number = models.CharField(max_length=32, blank=True)
