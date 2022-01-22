from etl_api_extract_data import get_planets_database

PLANETS_DATABASE = get_planets_database()
PLANET_MAIN_DATA_KEYS = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population']


def get_prepared_planets_database():
    prepared_planets_database = []

    for record in PLANETS_DATABASE:
        prepared_record = get_prepared_planet_data(record)
        prepared_planets_database.append(prepared_record)

    return prepared_planets_database


def get_prepared_planet_data(planet_data: dict):
    prepared_planet_data = dict()

    for key, value in planet_data.items():
        if key in PLANET_MAIN_DATA_KEYS:

            if key == 'diameter':
                prepared_planet_data[key] = get_prepared_diameter(value)
            elif key == 'surface_water':
                prepared_planet_data[key] = get_prepared_surface_water(value)
            elif key == 'population':
                prepared_planet_data[key] = get_prepared_population(value)
            else:
                prepared_planet_data[key] = value

    return prepared_planet_data


def get_prepared_diameter(diameter):
    prepared_diameter = diameter

    if diameter != "unknown":
        prepared_diameter = str("{:.3f}".format(int(diameter)/1000)) + " km"

    return prepared_diameter


def get_prepared_surface_water(coefficient):
    prepared_coefficient = coefficient

    if coefficient != "unknown":
        prepared_coefficient = str(coefficient) + " %"

    return prepared_coefficient


def get_prepared_population(amount):
    prepared_amount = amount

    if prepared_amount != "unknown":
        prepared_amount = str("{:,}".format(int(amount))) + ' people'

    return prepared_amount

