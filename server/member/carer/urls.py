from django.conf.urls import url

from .views import CarerDetails, CarerDependentList

urlpatterns = [
    url(r'^(?P<id>\d+)$', CarerDetails.as_view()),
    url(r'^(?P<id>\d+)/dependents', CarerDependentList.as_view())
]