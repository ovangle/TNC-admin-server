from rest_framework import generics

from .models import UserGroup
from .serializers import UserGroupSerializer

class UserGroupList(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class=UserGroupSerializer
