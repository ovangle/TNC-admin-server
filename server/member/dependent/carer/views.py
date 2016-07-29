from rest_framework import generics

from .models import Carer
from ..dependent.models import Dependent
from ..dependent.serializers import DependentSerializer
from .serializers import CarerSerializer

class CarerDetails(generics.RetrieveAPIView):
    queryset = Carer.objects.all()
    serializer_class = CarerSerializer

    lookup_url_kwarg = 'id'

class CarerDependentList(generics.ListAPIView):
    serializer_class = DependentSerializer 

    def get_queryset(self):
        carer_id = self.request.resolver_match.kwargs['id']
        return Dependent.objects.filter(carers__id=carer_id)

