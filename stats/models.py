from django.db import models


class CountryStats(models.Model):
    name = models.CharField(max_length=100)
    total_cases = models.IntegerField()
    new_cases = models.IntegerField()
    total_deaths = models.IntegerField()
    new_deaths = models.IntegerField()
    total_recovered = models.IntegerField()
    active_cases = models.IntegerField()
    serious_critical = models.IntegerField()
    total_cases_per_1m_population = models.IntegerField()
    deaths_per_1m_population = models.IntegerField()
    first_case = models.CharField(max_length=100)
