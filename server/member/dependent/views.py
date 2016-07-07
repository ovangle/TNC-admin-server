from rest_framework import generics

from .models import Dependent
from .serializers import DependentSerializer


class DependentList(generics.ListAPIView):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerializer