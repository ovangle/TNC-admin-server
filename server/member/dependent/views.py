from rest_framework import generics

from .models import Dependent
from .serializers import DependentSerializer


class DependentList(generics.ListCreateAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer

class DependentDetails(generics.RetrieveUpdateAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer
