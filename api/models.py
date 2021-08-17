from django.db import models

class CovidCases(models.Model):
    date = models.DateField()
    state = models.CharField(null=True, max_length=200)
    city = models.CharField(null=True, max_length=200)
    place_type = models.CharField(null=True, max_length=200)
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    order_for_place = models.IntegerField()
    is_last = models.BooleanField()
    estimated_population_2019 = models.IntegerField()
    estimated_population = models.IntegerField()
    city_ibge_code = models.IntegerField()
    confirmed_per_100k_inhabitants = models.FloatField()
    death_rate = models.FloatField()




