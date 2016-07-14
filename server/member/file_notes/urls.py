from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListCreateFileNotes.as_view()),
    url(r'^(?P<pk>\d+)$', views.UpdateFileNote.as_view())
]