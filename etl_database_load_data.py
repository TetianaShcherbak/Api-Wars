import database_common


@database_common.connection_handler
def set_new_user_record(cursor, email, password):
    cursor.execute(f"""
        INSERT INTO users(username, hashed_password)
        VALUES(%(email)s, %(password)s);""", {'email': email, 'password': password})

