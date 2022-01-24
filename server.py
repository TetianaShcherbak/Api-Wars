from flask import Flask, render_template, redirect, request, jsonify
from utils import hash_password, verify_password
import json
from etl_database_transform_data import get_prepared_planet_database_content, CONTENT_TABLE_HEADER
from etl_database_transform_data import get_prepared_planet_residents_content, CONTENT_RESIDENTS_TABLE_HEADER
from etl_database_extract_data import is_email_exists, get_password_by_email
from etl_database_load_data import set_new_user_record

app = Flask(__name__)
app.secret_key = '9e33e7321f59a3fdc954607f32c9da3f6b74ec0bc36828e0555de5a37987727a'


@app.route('/', methods=['POST', 'GET'])
def home_page():
    table_header = CONTENT_TABLE_HEADER
    table_content = get_prepared_planet_database_content()

    return render_template('index.html', header=table_header, content=table_content)


@app.route('/page/<page_id>', methods=['POST','GET'])
def show_page(page_id):
    table_header = CONTENT_TABLE_HEADER
    table_content = get_prepared_planet_database_content(page_id)

    return render_template('index.html', header=table_header, content=table_content)


@app.route('/planetResidents/<string:planet>', methods=['POST'])
def send_residents_data(planet):
    planet = json.loads(planet)['name']
    table_headers = CONTENT_RESIDENTS_TABLE_HEADER
    table_content = get_prepared_planet_residents_content(planet)
    residents_data = {
        "headers": table_headers,
        "content": table_content
    }

    return jsonify(residents_data)


@app.route('/registration', methods=['POST', 'GET'])
def registration_page():
    if request.method == 'POST':
        email = request.form['email']
        if is_email_exists(email):
            return '''<h1>Login already exists!</h1><br>
                        <form action='/registration'>
                            <button>Back to registration page</button>
                        </form>'''
        password = hash_password(request.form['password'])
        set_new_user_record(email, password)
        return redirect('/')
    else:
        return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    if is_email_exists(email):
        if verify_password(request.form['password'], get_password_by_email(email)):
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return '''<h1>User doesn't exist! Sign Up, please!</h1><br>
                                <form action='/registration'>
                                    <button>Go to registration page</button>
                                </form>'''


if __name__ == "__main__":

    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )


# @app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
# def processUserInfo(userInfo):
#     userInfo = json.loads(userInfo)
#     print()
#     print('USER INFO RECEIVED')
#     print('------------------')
#     print(f'UserName: {userInfo["name"]}')
#     print(f'User Type: {userInfo["type"]}')
#     print()
#
#     return"Info Received successfully"

