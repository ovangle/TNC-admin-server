from django.conf.urls import url, include

from .voucher import (urls as voucher_urls)

from .views import ActivityList

urlpatterns = [
    url(r'^$', ActivityList.as_view()),
    url(r'^voucher/', include(voucher_urls))
]