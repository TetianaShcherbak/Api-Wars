from flask import Flask, render_template, request, jsonify
import json
import etl_database_transform_data
from etl_database_transform_data import get_prepared_planet_database_content, CONTENT_TABLE_HEADER
from etl_database_transform_data import get_prepared_planet_residents_content, CONTENT_RESIDENTS_TABLE_HEADER

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
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

