from django.db import models

class ChemistVoucherManager(models.Manager):
    kind = 'activity::ChemistVoucher'

    def create(self, **kwargs):
        kwargs['kind'] = ChemistVoucherManager.kind
        return super(ChemistVoucherManager, self).create(**kwargs)

class FoodcareVoucherManager(models.Manager):
    kind = 'activity::FoodcareVoucher'

    def create(self, **kwargs):
        kwargs['kind'] = FoodcareVoucherManager.kind
        return super(FoodcareVoucherManager, self).create(**kwargs)

class EAPAVoucherManager(models.Manager):
    kind = 'activity::EAPAVoucher'

    def create(self, **kwargs):
        kwargs['kind'] = EPAPVoucherManager.kind
        return super(EAPAVoucherManager, self).create(**kind)