from rest_framework import generics

from .models import StaffMember
from .serializers import StaffMemberSerializer

class StaffMemberList(generics.ListAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer

    def create(self, request):
        return super(StaffMemberList, self).create(request) 

class StaffMemberDetails(generics.RetrieveUpdateAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
    lookup_url_kwarg = 'id'