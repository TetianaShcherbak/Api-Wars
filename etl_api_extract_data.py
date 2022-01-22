import requests

DATA_SOURCE = {'people': 'https://swapi.py4e.com/api/people/',
               'planets': 'https://swapi.py4e.com/api/planets/',
               'films': 'https://swapi.py4e.com/api/films/',
               'species': 'https://swapi.py4e.com/api/species/',
               'vehicles': 'https://swapi.py4e.com/api/vehicles/',
               'starships': 'https://swapi.py4e.com/api/starships/'}


def get_planets_database():
    response = requests.get(DATA_SOURCE['planets']).json()
    data = response['results']
    return data
