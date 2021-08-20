from django.urls import path
from .views import RawApiList, CityApiList, StateApiList, StatesLatestApiList

urlpatterns = [
    path('raw/', RawApiList.as_view()),
    path('city/', CityApiList.as_view()),
    path('state/', StateApiList.as_view()),
    path('state/latest/', StatesLatestApiList.as_view()),
]