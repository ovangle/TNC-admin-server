from django.db import models
from django.contrib.postgres.fields import ArrayField

from member.basic.models import EnergyAccountBill

from ..task.models import Task

from .managers import EAPAVoucherManager, FoodcareVoucherManager, ChemistVoucherManager
from .eapa_voucher_book import EAPAVoucherBook, EAPAVoucherBookField

class Voucher(models.Model):
    task = models.OneToOneField(Task)
    kind = models.CharField(max_length=32)

    def get_subkind_instance(self):
        if self.kind == EAPAVoucher.objects.kind:
            return self.eapavoucher
        elif self.kind == FoodcareVoucher.objects.kind:
            return self.foodcarevoucher
        elif self.kind == ChemistVoucher.objects.kind:
            return self.chemistvoucher
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

    def __init__(self, *args, **kwargs):
        super(ChemistVoucher, self).__init__(*args, **kwargs)
        self.kind = ChemistVoucher.objects.kind

    def get_subkind_instance(self):
        return self


class FoodcareVoucher(Voucher):
    objects = FoodcareVoucherManager()

    value = models.IntegerField()
    expires = models.DateField()

    redeemed = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(FoodcareVoucher, self).__init__(*args, **kwargs)
        self.kind = FoodcareVoucher.objects.kind

    def get_subkind_instance(self):
        return self

