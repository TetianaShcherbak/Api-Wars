import requests
import utils

DATA_SOURCE = {'people': 'https://swapi.py4e.com/api/people/',
               'planets': 'https://swapi.py4e.com/api/planets/',
               'films': 'https://swapi.py4e.com/api/films/',
               'species': 'https://swapi.py4e.com/api/species/',
               'vehicles': 'https://swapi.py4e.com/api/vehicles/',
               'starships': 'https://swapi.py4e.com/api/starships/'}

AMOUT_OF_RECORDS_ON_PAGE = 10


def get_data_for_planets_database():
    data = []
    response = get_api_response()
    response_amount = utils.get_round_up_number(response['count'], AMOUT_OF_RECORDS_ON_PAGE)
    data.append(response['results'])

    for page in range(1, response_amount):
        source = response['next']
        response = get_api_response(source)
        data.append(response['results'])

    return data


def get_api_response(source=DATA_SOURCE['planets']):
    response = requests.get(source).json()
    return response


def get_data_for_planet_residents_database():
    residents_data = []
    planets_data = get_data_for_planets_database()

    for page in planets_data:
        for planet in page:
            single_planet_residents = []
            planet_name = planet['name']
            planet_residents = planet['residents']
            for resident in planet_residents:
                resident_info = get_api_response(resident)
                resident_info['planet_name'] = planet_name
                single_planet_residents.append(resident_info)

            residents_data.append(single_planet_residents)

    return residents_data