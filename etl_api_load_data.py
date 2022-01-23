from etl_api_transform_data import get_prepared_planets_database
import database_common
from etl_database_extract_data import get_last_update_time_planets_database
import  psycopg2
from datetime import datetime, timedelta

PLANETS_DATABASE_CONTENT = get_prepared_planets_database()
UPDATE_DATABASE_TIME_DELTA = 4


def refresh_planets_database(time_delta=UPDATE_DATABASE_TIME_DELTA):
    current_time = datetime.now()
    last_update_time = get_last_update_time_planets_database()
    if last_update_time is None:
        last_update_time = "2022-01-01 00:00:00"
    delta = timedelta(hours=time_delta)
    next_update_time = datetime.strptime(last_update_time, "%Y-%m-%d %H:%M:%S") + delta
    if current_time > next_update_time:
        insert_planets_database(current_time.strftime("%Y-%m-%d %H:%M:%S"))


def insert_planets_database(update_time):

    for planet in PLANETS_DATABASE_CONTENT:
        row_content = []
        for key, value in planet.items():
            row_content.append(value)
        row_content.append(update_time)
        try:
            set_single_planet_record(row_content)
        except psycopg2.errors.UniqueViolation:
            update_single_planet_record(row_content)


@database_common.connection_handler
def set_single_planet_record(cursor, content):
    name = content[0]
    diameter = content[1]
    climate = content[2]
    terrain = content[3]
    surface_water = content[4]
    population = content[5]
    last_update_time = content[6]

    cursor.execute("""
                    INSERT INTO planets(name, diameter, climate, terrain, surface_water, population, last_update_time)
                    VALUES (%(name)s, %(diameter)s, %(climate)s, %(terrain)s, %(surface_water)s, %(population)s, %(last_update_time)s)
               """, {'name': name, 'diameter': diameter, 'climate': climate, 'terrain': terrain, 'surface_water': surface_water, 'population': population, 'last_update_time': last_update_time})


@database_common.connection_handler
def update_single_planet_record(cursor, content):
    name = content[0]
    diameter = content[1]
    climate = content[2]
    terrain = content[3]
    surface_water = content[4]
    population = content[5]
    last_update_time = content[6]

    cursor.execute("""
                    UPDATE planets
                    SET diameter = %(diameter)s, 
                        climate = %(climate)s, 
                        terrain = %(terrain)s, 
                        surface_water = %(surface_water)s, 
                        population = %(population)s,
                        last_update_time = %(last_update_time)s
                    WHERE name = %(name)s
               """, {'name': name, 'diameter': diameter, 'climate': climate, 'terrain': terrain, 'surface_water': surface_water, 'population': population, 'last_update_time': last_update_time})

