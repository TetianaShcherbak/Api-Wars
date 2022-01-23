import requests
import utils

DATA_SOURCE = {'people': 'https://swapi.py4e.com/api/people/',
               'planets': 'https://swapi.py4e.com/api/planets/',
               'films': 'https://swapi.py4e.com/api/films/',
               'species': 'https://swapi.py4e.com/api/species/',
               'vehicles': 'https://swapi.py4e.com/api/vehicles/',
               'starships': 'https://swapi.py4e.com/api/starships/'}

AMOUT_OF_RECORDS_ON_PAGE = 10


def get_planets_database():
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
