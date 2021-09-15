from django.urls import path
from django.urls.conf import re_path
from .views import RawApiList
from .state.views import StateApiList, StatesLatestApiList, StateLastYearApiList, StateLastMonthApiList
from .city.views import CityApiList, CityLastYearApiList, CityLastMonthApiList, CitySearchApiList

urlpatterns = [
    path('raw/', RawApiList.as_view()),
] + [
    re_path('city/(?P<city>.+)/last_year/', CityLastYearApiList.as_view()),
    re_path('city/(?P<city>.+)/last_month/', CityLastMonthApiList.as_view()),
    re_path('city/(?P<city>.+)/(?P<state>.+)/', CityApiList.as_view()),
    path('city/', CitySearchApiList.as_view()),
] + [
    re_path('state/(?P<state>.+)/last_year/', StateLastYearApiList.as_view()),
    re_path('state/(?P<state>.+)/last_month/', StateLastMonthApiList.as_view()),
    re_path('state/(?P<state>.+)/$', StateApiList.as_view()),
] + [
    path('latest/state/', StatesLatestApiList.as_view()),
]