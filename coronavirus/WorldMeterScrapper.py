import requests
from bs4 import BeautifulSoup

# Collect the worldometers page
page = requests.get('https://www.worldometers.info/coronavirus/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(id="main_table_countries_today")
table = soup.find('tbody')


def refactor_data( country_data):
    '''

    :param country_data:
    :return: cleaned data dictionary
    '''
    if country_data[2] != ' ' and country_data[2] != '':
        country_data[2] = int(country_data[2][1:].replace(',', ''))
    else:
        country_data[2] = 0
    if country_data[4] != ' ' and country_data[4] != '':
        country_data[4] = int(country_data[4][1:].replace(',', ''))
    else:
        country_data[4] = 0
    int_fields = [1, 3, 5, 6, 7]
    float_fields = [8, 9]
    for i in int_fields:
        if country_data[i] != ' ' and country_data[i] != '':
            country_data[i] = int(country_data[i].replace(',', ''))
        else:
            country_data[i] = 0
    for i in float_fields:
        if country_data[i] != ' ' and country_data[i] != '':
            country_data[i] = float(country_data[i].replace(',', ''))
        else:
            country_data[i] = 0
    td_dict = {
        'name': country_data[0],
        'total_cases': country_data[1],
        'new_cases': country_data[2],
        'total_deaths': country_data[3],
        'new_deaths': country_data[4],
        'total_recovered': country_data[5],
        'active_cases': country_data[6],
        'serious_critical': country_data[7],
        'total_cases_per_1m_population': country_data[8],
        'deaths_per_1m_population': country_data[9],
        'first_case': country_data[10],
    }
    return td_dict


def get_data():
    '''
    our data is a table  every row represent a country
    we iterate over the countries << rows or trs >>
    then over the columns << data tds >>
    '''
    global_data = []
    trs = table.find_all('tr')
    for i in range(len(trs)):
        tds = trs[i].find_all('td')
        country_data = []
        for td in tds:
            country_data.append(td.text)
        country_data = refactor_data(country_data)
        global_data.append(country_data)
    return global_data
