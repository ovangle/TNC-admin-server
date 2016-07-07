from rest_framework import generics

from .models import Voucher
from .serializers import VoucherSerializer

class VoucherList(generics.ListCreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

    def get_queryset(self):
        qs = super(VoucherList, self).get_queryset()
        member_id = int(self.request.query_params.get('member'))
        return qs.filter(member_id=member_id).order_by('-date_issued')



