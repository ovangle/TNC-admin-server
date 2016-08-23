from django.db import models
from ext.django.fields import EnumField

from ..address.models import Address
from ..name.models import Name

from .energy_retailer import EnergyRetailer
from .account_type import EnergyAccountType

from .managers import GasAccountManager, ElectricityAccountManager

class EnergyAccount(models.Model):
    kind = 'member.basic::EnergyAccount'

    objects = models.Manager()
    gas_accounts = GasAccountManager()
    electricity_accounts = ElectricityAccountManager()

    type = EnumField(enum_type=EnergyAccountType)
    retailer = EnumField(enum_type=EnergyRetailer)
    account_number = models.CharField(max_length=128, blank=True)

class EnergyAccountBill(models.Model):
    account = models.OneToOneField(EnergyAccount)
    value = models.DecimalField(max_digits=7, decimal_places=2) 

