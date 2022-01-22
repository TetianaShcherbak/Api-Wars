import database_common


@database_common.connection_handler
def get_last_update_time_planets_database(cursor):
    cursor.execute("""SELECT DISTINCT last_update_time from planets""")
    return dict(cursor.fetchone())['last_update_time']