from django.db import models

class CovidCases(models.Model):
    report_date = models.DateField(null=True)
    state = models.CharField(null=True, max_length=200)
    city = models.CharField(null=True, max_length=200)
    place_type = models.CharField(null=True, max_length=200)
    confirmed = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    order_for_place = models.IntegerField(null=True)
    is_last = models.BooleanField(null=True)
    estimated_population_2019 = models.IntegerField(null=True)
    estimated_population = models.IntegerField(null=True)
    city_ibge_code = models.IntegerField(null=True)
    confirmed_per_100k_inhabitants = models.FloatField(null=True)
    death_rate = models.FloatField(null=True)




