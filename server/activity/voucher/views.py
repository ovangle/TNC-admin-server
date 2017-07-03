import dateutil.parser

from rest_framework import generics

from .models import Voucher
from .serializers import (
    VoucherSerializer,
    ChemistVoucherSerializer,
    EAPAVoucherSerializer,
    FoodcareVoucherSerializer
)    

class VoucherList(generics.ListAPIView):
    serializer = VoucherSerializer

    def get_queryset(self):
        voucher_type = self.request.query_params.get('voucher')
        if voucher_type is 'CHEMIST':
            qs = ChemistVoucher.objects.all()
        else:
            qs = Voucher.objects.all()

        member_id = self.request.query_params.get('member')
        if member_id is not None:
            qs = qs.filter(task__member__id=member_id)

        before_datestr = self.request.query_params.get('before')
        try:
            before_date = dateutil.parser.parse(before_datestr)
            qs = qs.filter(task__at__before=before_date)
        except ValueError:      
            pass

        after_datestr = self.request.query_params.get('after')      
        try:
            after_date = dateutil.parser.parse(before_datestr)
            qs = qs.filter(task__at__after=after_date)
        except ValueError:
            pass

        qs = qs.order_by('-task__at')
        return qs

    def get_serializer(self, instance=None, data=None, partial=False):
        serializer = None
        if instance is None:     
            raise ValueError('VoucherList can only be instantiated with an instance')
        return VoucherSerializer.for_instance(instance, data=data)

class ChemistVoucherCreate(generics.CreateAPIView):
    serializer = ChemistVoucherSerializer

class FoodcareVoucherCreate(generics.CreateAPIView):    
    serializer = FoodcareVoucherSerializer

class EAPAVoucherCreate(generics.CreateAPIView):    
    serializer = EAPAVoucherSerializer


