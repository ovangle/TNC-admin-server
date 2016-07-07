from rest_framework import generics

from .models import Partner
from .serializers import PartnerSerializer

class PartnerDetails(generics.RetrieveUpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    def get_object(self, request):
        member_id = request.params.get('id')


