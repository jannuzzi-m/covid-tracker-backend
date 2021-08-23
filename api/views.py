from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import CovidCases
from .serializers import RawCasesSerializer


class RawApiList(generics.ListAPIView):
    serializer_class = RawCasesSerializer
    pagination_class = PageNumberPagination
    queryset = CovidCases.objects.filter(is_last=True).order_by('-report_date')


class CityApiList(generics.ListAPIView):
    serializer_class = RawCasesSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        city = self.kwargs['city']
        queryset = CovidCases.objects.filter(place_type='city', city=city,).order_by('-report_date')
        return queryset
    

class StateApiList(generics.ListAPIView):
    serializer_class = RawCasesSerializer
    pagination_class = PageNumberPagination
    

    def get_queryset(self):
        state = self.kwargs['state'].upper()
        queryset = CovidCases.objects.filter(place_type='state', state=state).order_by('-report_date')
        return queryset

        
class StatesLatestApiList(generics.ListAPIView):
    queryset = CovidCases.objects.filter(place_type='state', is_last=True)
    serializer_class = RawCasesSerializer
    pagination_class = None


