from django.conf.urls import url, include

from .induction_survey.views import StaffInductionSurveyDetails
from .views import StaffMemberList, StaffMemberDetails


urlpatterns = [
    url(r'^$', StaffMemberList.as_view()),
    url(r'^(?P<id>\d+)/', include([
        url(r'^$', StaffMemberDetails.as_view()),
        url(r'^induction_survey$', StaffInductionSurveyDetails.as_view())
    ]))
]
