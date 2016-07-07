from django.db import models


from .eapa.models import EAPAAssessment
from .managers import EAPAVoucherManager, FoodcareVoucherManager

class Voucher(models.Model):
    date_issued = models.DateField()
    member = models.ForeignKey('member.Member')
    kind = models.CharField(max_length=32)

    def get_subkind_instance(self):
        if self.kind == EAPAVoucher.objects.kind:
            return self.eapavoucher
        elif self.kind == FoodcareVoucher.objects.kind:
            return self.foodcarevoucher
        else:
            raise ValueError('Invalid kind on voucher: {0}'.format(self.kind))

class EAPAVoucher(Voucher):
    objects = EAPAVoucherManager()
    assessment = models.OneToOneField(EAPAAssessment)

    def get_subkind_instance(self):
        return self

class FoodcareVoucher(Voucher):
    objects = FoodcareVoucherManager()

    value = models.IntegerField()
    expires = models.DateField()

    redeemed = models.BooleanField(default=False)

    def get_subkind_instance(self):
        return self
