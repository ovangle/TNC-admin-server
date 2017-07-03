from django.conf.urls import url, include

from .views import (
    VoucherList,
    ChemistVoucherCreate,
    EAPAVoucherCreate,
    FoodcareVoucherCreate
)    

urlpatterns = [
    url(r'^$', VoucherList.as_view()),
    url(r'^chemist$', ChemistVoucherCreate.as_view()),
    url(r'^eapa$', EAPAVoucherCreate.as_view()),
    url(r'^foodcare$', FoodcareVoucherCreate.as_view())
]