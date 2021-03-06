from etl_api_extract_data import get_data_for_planets_database, get_data_for_planet_residents_database

PLANETS_DATABASE = get_data_for_planets_database()
RESIDENTS_DATABASE = get_data_for_planet_residents_database()

PLANET_MAIN_DATA_KEYS = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population']
RESIDENT_MAIN_DATA_KEYS = ['name', 'height', 'mass', 'skin_color', 'hair_color', 'eye_color', 'birth_year', 'gender', 'planet_name']


def get_prepared_data_for_planets_database():
    prepared_data_for_planets_database = []

    for page in PLANETS_DATABASE:
        for record in page:
            prepared_record = get_prepared_planet_data(record)
            prepared_data_for_planets_database.append(prepared_record)

    return prepared_data_for_planets_database


def get_prepared_data_for_planet_residents_database():
    prepared_data_for_planet_residents_database = []

    for page in RESIDENTS_DATABASE:
        for record in page:
            prepared_record = get_prepared_resident_data(record)
            prepared_data_for_planet_residents_database.append(prepared_record)

    return prepared_data_for_planet_residents_database


def get_prepared_resident_data(resident_data: dict):
    prepared_resident_data = dict()

    for key, value in resident_data.items():
        if key in RESIDENT_MAIN_DATA_KEYS:

            if key == 'height':
                prepared_resident_data[key] = get_prepared_height(value)
            elif key == 'mass':
                prepared_resident_data[key] = get_prepared_mass(value)
            else:
                prepared_resident_data[key] = value

    return prepared_resident_data


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


def get_prepared_height(height):
    prepared_height = height

    if height == "none":
        return prepared_height

    if height != "unknown":
        prepared_height = str(int(height)/100) + ' m'

    return prepared_height


def get_prepared_mass(mass):
    prepared_mass = mass

    if mass != "unknown":
        prepared_mass = mass + ' kg'

    return prepared_mass
