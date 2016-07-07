from django.db import models


class EAPAVoucherManager(models.Manager):
    kind = 'member.voucher::EAPAVoucher'

    def create(self, **kwargs):
        kwargs['kind'] = EAPAVoucherManager.kind
        return super(EAPAVoucherManager, self).create(**kwargs)

class FoodcareVoucherManager(models.Manager):
    kind = 'member.voucher::FoodcareVoucher'

    def create(self, **kwargs):
        kwargs['kind'] = FoodcareVoucherManager.kind
        return super(FoodcareVoucher, self).create(**kwargs)


