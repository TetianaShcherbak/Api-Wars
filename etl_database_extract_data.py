import database_common


@database_common.connection_handler
def get_last_update_time_planets_database(cursor):
    cursor.execute("""SELECT DISTINCT last_update_time from planets""")
    result = cursor.fetchone()
    if result:
        return dict(result)['last_update_time']
    else:
        return None


@database_common.connection_handler
def get_last_update_time_planet_residents_database(cursor):
    cursor.execute("""SELECT DISTINCT last_update_time from planet_residents""")
    result = cursor.fetchone()
    if result:
        return dict(result)['last_update_time']
    else:
        return None


@database_common.connection_handler
def get_planet_database_content(cursor, start_row_number, row_amount):
    cursor.execute(f"""
        SELECT * FROM  planets
        ORDER BY id
        LIMIT {row_amount} OFFSET {start_row_number}""")
    return cursor.fetchall()
