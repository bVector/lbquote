from flask import Flask
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    price = requests.get('https://coinbase.com/api/v1/prices/buy').json()
    return str(price['total']['amount'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
