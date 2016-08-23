from django.db import models
from .account_type import EnergyAccountType

class GasAccountManager(models.Manager):
    def get_queryset(self):
        qs = super(GasAccountManager, self).get_queryset()
        return qs.filter(type=EnergyAccountType.gas)

    def create(self, retailer=None, account_number=''):
        return super(GasAccountManager, self).create(
            type=EnergyAccountType.gas,
            retailer=retailer,
            account_number=account_number
        )

class ElectricityAccountManager(models.Manager):  
    def get_queryset(self):
        qs = super(ElectricityAccountManager, self).get_queryset()
        return qs.filter(type=ElectricityAccountType.electricity)

