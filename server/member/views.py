
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        qs = super(MemberList, self).get_queryset()
        qs = qs.order_by('-updated')
        return qs

    def list(self, request):
        return super(MemberList, self).list(request)

    def create(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetails(generics.RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_url_kwarg = 'id'
