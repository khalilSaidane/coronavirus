# this script should be run to init the database
from stats.models import CountryStats
from coronavirus.WorldMeterScrapper import get_data

data = get_data()

for country in data:
    country_stats = CountryStats(name=country['name'],
                                 total_cases=country['total_cases'],
                                 new_cases=country['new_cases'],
                                 total_deaths=country['total_deaths'],
                                 new_deaths=country['new_deaths'],
                                 total_recovered=country['total_recovered'],
                                 active_cases=country['active_cases'],
                                 serious_critical=country['serious_critical'],
                                 total_cases_per_1m_population=country['total_cases_per_1m_population'],
                                 deaths_per_1m_population=country['deaths_per_1m_population'],
                                 first_case=country['first_case']
                                 )
    country_stats.save()
