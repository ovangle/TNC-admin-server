from django.conf.urls import url, include

from . import views

import member.voucher.urls
import member.file_notes.urls
import member.dependent.urls

urlpatterns = [
    url(r'^$', views.MemberList.as_view()),
    url(r'^(?P<id>\d+)$', views.MemberDetails.as_view()),
    url(r'^voucher/', include(member.voucher.urls)),
    url(r'^filenote/', include(member.file_notes.urls)),
    url(r'^dependent/', include(member.dependent.urls))
]