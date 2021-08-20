from rest_framework import serializers
from .models import CovidCases

class RawCasesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CovidCases
        fields = '__all__'