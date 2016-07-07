from rest_framework import serializers
from ext.rest_framework.serializers import GenericSerializer

from .eapa.serializers import EAPAAssessmentSerializer

from .models import EAPAVoucher, FoodcareVoucher


class VoucherSerializer(GenericSerializer):
    member_id = serializers.IntegerField()
    date_issued = serializers.DateField()

    @property
    def subkinds(self):
        return {
            EAPAVoucher.objects.kind: EAPAVoucherSerializer,
            FoodcareVoucher.objects.kind: FoodcareVoucherSerializer
        }

class EAPAVoucherSerializer(VoucherSerializer):
    assessment = EAPAAssessmentSerializer()


class FoodcareVoucherSerializer(VoucherSerializer):
    value = serializers.IntegerField()
    expires = serializers.DateField()
    redeemed = serializers.BooleanField()


