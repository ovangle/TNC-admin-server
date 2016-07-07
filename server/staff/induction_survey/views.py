from rest_framework import generics, mixins 

from ..models import StaffMember 
from .serializers import StaffInductionSurveySerializer

class StaffInductionSurveyDetails(generics.GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = StaffInductionSurveySerializer
    queryset = StaffMember.objects.all()
    lookup_url_kwarg = 'staff_id'

    def get_object(self):
        user = super(UserInductionSurveyDetails, self).get_object()
        return user.induction_survey


