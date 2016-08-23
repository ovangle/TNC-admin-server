from django.conf.urls import url, include

from .views import ActivityList, ActivityDetails

urlpatterns = [
    url(r'^$', ActivityList.as_view()),
    url(r'^(?P<id>\d+)$', ActivityDetails.as_view())
]