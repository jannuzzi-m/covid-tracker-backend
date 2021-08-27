from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from ..models import CovidCases
from ..serializers import RawCasesSerializer


class StateApiList(generics.ListAPIView):
    """
        Returns all the results of a given state paginated
    """
    serializer_class = RawCasesSerializer
    pagination_class = PageNumberPagination
    

    def get_queryset(self):
        state = self.kwargs['state'].upper()
        queryset = CovidCases.objects.filter(place_type='state', state=state).order_by('-report_date')
        return queryset

        
class StatesLatestApiList(generics.ListAPIView):
    """
        Returns the last result of all 27 states
    """
    queryset = CovidCases.objects.filter(place_type='state', is_last=True)
    serializer_class = RawCasesSerializer
    pagination_class = None


class StateLastYearApiList(generics.ListAPIView):
    """
        Return the result of the first day of the last 12 months of the given state
    """
    serializer_class = RawCasesSerializer
    pagination_class = None


    def get_queryset(self):
        queryset = CovidCases.objects.raw(f"select * from api_covidcases where state = '{self.kwargs['state'].upper()}' and place_type = 'state' and date_part('day', report_date) = 1 order by report_date desc limit 12; ")
        return queryset


class StateLastMonthApiList(generics.ListAPIView):
    """
        Returns the last 30 results of given state
    """
    serializer_class = RawCasesSerializer
    pagination_class = None


    def get_queryset(self):
            state = self.kwargs['state'].upper()
            queryset = CovidCases.objects.filter(place_type='state', state=state).order_by('-report_date')[:30]
            return queryset
