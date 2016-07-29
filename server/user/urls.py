from django.conf.urls import url, include

from .views import SuggestUniqueUsername, CreateUser, LoginUser, InitializeContext
from .group.views import UserGroupList

urlpatterns = [
    url(r'^login$', LoginUser.as_view()),
    url(r'^suggest_username$', SuggestUniqueUsername.as_view()),
    url(r'^groups$', UserGroupList.as_view()),
    url(r'^initialize$', InitializeContext.as_view())
]