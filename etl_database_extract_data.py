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


@database_common.connection_handler
def get_planet_residents_amount(cursor,planet_name):
    cursor.execute(f"""
        SELECT COUNT(name) FROM planet_residents
        GROUP BY  planet_name
        HAVING planet_name='{planet_name}'""")
    result = cursor.fetchone()
    if result:
        return dict(result)['count']
    else:
        return None


@database_common.connection_handler
def get_planet_residents_data(cursor, planet_name):
    cursor.execute(f"""
            SELECT * FROM planet_residents
            WHERE planet_name='{planet_name}'""")

    return cursor.fetchall()\


@database_common.connection_handler
def is_email_exists(cursor, email):
    cursor.execute("""
        SELECT username FROM users
        WHERE username=%(email)s;""", {'email': email})

    email = cursor.fetchone()
    return email is not None


@database_common.connection_handler
def get_password_by_email(cursor, email):
    cursor.execute("""
        SELECT hashed_password FROM users
        WHERE username=%(email)s;""", {'email': email})

    hashed_password = cursor.fetchone()
    print(hashed_password)
    print(dict(hashed_password)['hashed_password'])
    return dict(hashed_password)['hashed_password']

