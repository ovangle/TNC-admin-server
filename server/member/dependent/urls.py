from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DependentList.as_view()),
    url(r'^(?P<id>\d+)', views.DependentDetails.as_view())
]