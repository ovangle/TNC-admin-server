from rest_framework import generics


from .models import Task
from .serializers import TaskSerializer

class ActivityList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer 
    queryset = Task.objects.all()

    def get_queryset(self):
        qs = super(ActivityList, self).get_queryset()

        qs = qs.order_by('-at')

        member_id = self.request.query_params.get('member')
        if member_id is not None:
            qs = qs.filter(member__id=member_id)

        return qs

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(staff_member=user.staffmember)


class ActivityDetails(generics.RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_url_kwarg = 'id'


