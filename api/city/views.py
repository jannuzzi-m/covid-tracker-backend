from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

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
        queryset = CovidCases.objects.filter(place_type='city', city=city,).order_by('-report_date')
        return queryset


class CityLastYearApiList(generics.ListAPIView):
    """
        Return the result of the first day of the last 12 months of the given city
    """
    serializer_class = RawCasesSerializer
    pagination_class = None


    def get_queryset(self):
        queryset = CovidCases.objects.raw(f"select * from api_covidcases where city = '{self.kwargs['city'].capitalize()}' and place_type = 'city' and date_part('day', report_date) = 1 order by report_date desc limit 12; ")
        return queryset


class CityLastMonthApiList(generics.ListAPIView):
    """
        Returns the last 30 results of given city
    """
    serializer_class = RawCasesSerializer
    pagination_class = None


    def get_queryset(self):
            city = self.kwargs['city'].capitalize()
            queryset = CovidCases.objects.filter(place_type='city', city=city).order_by('-report_date')[:30]
            return queryset
