from flask import Flask, render_template, request, url_for, redirect
import requests
import swapi

app = Flask(__name__)
response = requests.get('https://api.github.com/repos/atom/atom').json()

print(response['stargazers_count'])

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )