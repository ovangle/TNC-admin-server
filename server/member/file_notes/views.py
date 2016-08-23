from rest_framework import generics, exceptions
from rest_framework.response import Response

from .models import MemberFileNote
from .serializers import MemberFileNoteSerializer

class QueryParamRequired(exceptions.APIException):
    status_code = 403
    default_detail = 'Missing query parameter'


class ListCreateFileNotes(generics.ListCreateAPIView):
    queryset = MemberFileNote.objects.all()
    serializer_class = MemberFileNoteSerializer

    def get_queryset(self): 
        qs = super(ListCreateFileNotes, self).get_queryset()
        qs = qs.order_by('-created')

        member_id = self.request.query_params.get('member')
        if member_id is not None:
            qs = qs.filter(member_id=member_id)

        staff_id = self.request.query_params.get('staff')
        if staff_id is not None:
            qs = qs.filter(staff_id=staff_id)

        pinned = (self.request.query_params.get('pinned') == 'true')
        if pinned:
            qs = qs.filter(pinned=pinned)

        created_before = self.request.query_params.get('before')
        if created_before is not None:
            qs = qs.filter(created__date__lt=created_before)

        created_after = self.request.query_params.get('after') 
        if created_after is not None:
            qs = qs.filter(created__date__gt=created_after)

        return qs

    def perform_create(self, serializer):
        user = self.request.user
        if not user.staffmember:
            raise exceptions.APIException(status=400, detail='User is not a staff member')
        serializer.save(staff=user.staffmember)


class UpdateFileNote(generics.UpdateAPIView):
    queryset = MemberFileNote.objects.all()
    serializer_class = MemberFileNoteSerializer

    def perform_update(self, serializer):
        user = self.request.user
        if not user.staffmember:
            raise exceptions.APIException(status=400, detail='User is not a staff member')
        serializer.save(staff=user.staffmember)

