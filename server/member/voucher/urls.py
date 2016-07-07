from django.conf.urls import url

from .views import VoucherList

urlpatterns = [
    url(r'^$', VoucherList.as_view())
]

