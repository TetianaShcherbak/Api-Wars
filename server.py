from flask import Flask, render_template, request, url_for, redirect
import json
import etl_api_load_data
from etl_database_transform_data import get_predared_planet_database_content, CONTENT_TABLE_HEADER

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home_page():
    table_header = CONTENT_TABLE_HEADER
    table_content = get_predared_planet_database_content()

    return render_template('index.html', header=table_header, content=table_content)


@app.route('/page/<page_id>', methods=['POST','GET'])
def previous_page(page_id):
    table_header = CONTENT_TABLE_HEADER
    start_row_number = int(page_id) * 10 - 10
    table_content = get_predared_planet_database_content(start_row_number)

    return render_template('index.html', header=table_header, content=table_content)


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


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
