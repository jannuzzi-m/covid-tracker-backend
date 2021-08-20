from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from .models import CovidCases
from .serializers import RawCasesPaginated


class RawApiList(generics.ListAPIView):
    serializer_class = RawCasesPaginated
    pagination_class = PageNumberPagination
    queryset = CovidCases.objects.filter(is_last=True).order_by('report_date')


class CityApiList(generics.ListAPIView):
    queryset = CovidCases.objects.filter(place_type = "city",).order_by('report_date')
    filter_backends = [SearchFilter]
    serializer_class = RawCasesPaginated
    pagination_class = PageNumberPagination
    search_fields = ['city']
    

class StateApiList(generics.ListAPIView):
    queryset = CovidCases.objects.filter(place_type = "state",).order_by('report_date')
    filter_backends = [SearchFilter]
    serializer_class = RawCasesPaginated
    pagination_class = PageNumberPagination
    search_fields = ['state']
    

