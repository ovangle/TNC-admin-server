from rest_framework import generics

from .models import StaffMember
from .serializers import StaffMemberSerializer

class StaffMemberList(generics.ListCreateAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer

    def get_serializer_class(self): 
        if self.request.method == 'GET':
            return StaffMemberSerializer
        else:
            return CreateRequestSerializer


class StaffMemberDetails(generics.RetrieveUpdateAPIView):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
    lookup_url_kwarg = 'id'