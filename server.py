from flask import Flask, render_template, request, url_for, redirect
import json
import etl_api_load_data

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


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
    etl_api_load_data.refresh_planets_database()
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )