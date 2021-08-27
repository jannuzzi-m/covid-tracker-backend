from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import CovidCases
from .serializers import RawCasesSerializer


class RawApiList(generics.ListAPIView):
    """
        Returns all the results paginated ordered by date
    """
    serializer_class = RawCasesSerializer
    pagination_class = PageNumberPagination
    queryset = CovidCases.objects.filter(is_last=True).order_by('-report_date')

