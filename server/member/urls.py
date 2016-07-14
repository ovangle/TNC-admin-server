from django.conf.urls import url, include

from . import views

import member.carer.urls
import member.voucher.urls
import member.file_notes.urls

urlpatterns = [
    url(r'^$', views.MemberList.as_view()),
    url(r'^(?P<id>\d+)$', views.MemberDetails.as_view()),
    url(r'^carer/', include(member.carer.urls)),
    url(r'^voucher/', include(member.voucher.urls)),
    url(r'^filenote/', include(member.file_notes.urls)),
]