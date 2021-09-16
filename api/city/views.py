from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from ..models import CovidCases
from ..serializers import RawCasesSerializer


class CityApiList(generics.ListAPIView):
    """
        Returns all the results of a given city paginated
    """
    serializer_class = RawCasesSerializer
    pagination_class = PageNumberPagination


    def get_queryset(self):
        city = self.kwargs['city']
        state = self.kwargs['state']
        queryset = CovidCases.objects.filter(place_type='city', city=city, state=state.upper()).order_by('-report_date')
        return queryset


class CityLastYearApiList(generics.ListAPIView):
    """
        Return the result of the first day of the last 12 months of the given city
    """
    serializer_class = RawCasesSerializer
    pagination_class = None


    def get_queryset(self):
        queryset = CovidCases.objects.raw(f"select * from api_covidcases where city = '{self.kwargs['city']}' and and state={self.kwargs['city'].upper()} place_type = 'city' and date_part('day', report_date) = 1 order by report_date desc limit 12; ")
        return queryset


class CityLastMonthApiList(generics.ListAPIView):
    """
        Returns the last 30 results of given city
    """
    serializer_class = RawCasesSerializer
    pagination_class = None


    def get_queryset(self):
            city = self.kwargs['city']
            state = self.kwargs['state']
            queryset = CovidCases.objects.filter(place_type='city', city=city, state=state).order_by('-report_date')[:30]
            return queryset


class CitySearchApiList(generics.ListAPIView):
    """
        Returns the search results for city 
    """
    queryset = CovidCases.objects.all().distinct('city')
    serializer_class = RawCasesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city']

