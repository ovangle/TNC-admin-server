from rest_framework import generics


from .models import Task, Voucher
from .serializers import ActivitySerializer

class ActivityList(generics.ListAPIView):
    serializer_class = ActivitySerializer 
    queryset = Task.objects.all()

    def get_queryset(self):
        qs = Task.objects.all()

        member_id = self.request.query_params.get('member')
        if member_id is not None:
            qs = qs.filter(member__id=member_id)

        staff_member_id = self.request.query_params.get('staff')
        if staff_member_id is not None:
            qs = qs.filter(staff__id=staff_member_id)

        qs = (qs
            .select_related('voucher')
            .order_by('-at')
        )     

        return qs

