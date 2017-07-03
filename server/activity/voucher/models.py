from datetime import date
from dateutil import relativedelta

from django.db import models
from django.contrib.postgres.fields import ArrayField

from member.basic.models import EnergyAccountBill

from ..task.models import Task

from .managers import EAPAVoucherManager, FoodcareVoucherManager, ChemistVoucherManager
from .eapa_voucher_book import EAPAVoucherBook, EAPAVoucherBookField
from chemist.models import ChemistPrescription

class Voucher(models.Model):
    task = models.OneToOneField(Task)
    kind = models.CharField(max_length=32)

    vouchers_in_financial_year = models.IntegerField() 

    def get_subkind_instance(self):
        if self.kind.endswith('FoodcareVoucher'):
            return self.foodcarevoucher
        elif self.kind.endswith('ChemistVoucher'):
            return self.chemistvoucher
        elif self.kind.endswith('EAPAVoucher'):     
                return self.eapavoucher
        else:
            raise ValueError('Invalid kind on voucher: {0}'.format(self.kind))
            

class EAPAVoucher(Voucher):
    objects = EAPAVoucherManager()

    gas_bill = models.OneToOneField(EnergyAccountBill, null=True, related_name='+')
    electricity_bill = models.OneToOneField(EnergyAccountBill, null=True, related_name='+')

    is_denying_basic_needs = models.BooleanField()
    is_facing_disconnection = models.BooleanField()
    is_disconnected = models.BooleanField()

    is_granted_limit_exemption = models.BooleanField()
    limit_exemption_description = models.TextField()

    is_customer_declaration_signed = models.BooleanField()
    is_assessor_declaration_signed = models.BooleanField()

    voucher_books = ArrayField(
        base_field=EAPAVoucherBookField(),
        default=list
    )

    def __init__(self, *args, **kwargs):
        super(EAPAVoucher, self).__init__(*args, **kwargs)
        self.kind = EAPAVoucher.objects.kind

    def get_subkind_instance(self):
        return self

    def bills(self):
        bills = {}
        if self.gas_bill is not None:
            bills['GAS'] = self.gas_bill
        if self.electricity_bill is not None:    
            bills['ELECTRICITY'] = self.electricity_bill
        return bills 

class ChemistVoucher(Voucher):
    objects = ChemistVoucherManager()

    prescription = models.OneToOneField(ChemistPrescription)

    is_granted_limit_exemption = models.BooleanField(default=False)
    limit_exemption_description = models.TextField(default='')

    is_assessor_declaration_signed = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(ChemistVoucher, self).__init__(*args, **kwargs)
        self.kind = ChemistVoucher.objects.kind

    def get_subkind_instance(self):
        return self

    @property
    def assessed_value(self):
        raw_value = self.prescription.value
        if raw_value <= 30.00 or self.is_granted_limit_exemption:
            return raw_value 
        return 30.00

def foodcare_voucher_expires():
    """ A foodcare voucher expires exactly one month after the date of issue"""
    return date.today() + relativedelta.relativedelta(month=1)

class FoodcareVoucher(Voucher):
    objects = FoodcareVoucherManager()

    value = models.IntegerField()
    expires = models.DateField(default=foodcare_voucher_expires)

    redeemed = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(FoodcareVoucher, self).__init__(*args, **kwargs)
        self.kind = FoodcareVoucher.objects.kind

    def get_subkind_instance(self):
        return self

