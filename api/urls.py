from django.urls import path
from django.urls.conf import re_path
from .views import RawApiList, CityApiList, StateApiList, StatesLatestApiList

urlpatterns = [
    path('raw/', RawApiList.as_view()),
    re_path('city/(?P<city>.+)/$', CityApiList.as_view()),
    path('state/latest/', StatesLatestApiList.as_view()),
    re_path('state/(?P<state>.+)/$', StateApiList.as_view()),
]