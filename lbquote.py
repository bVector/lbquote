from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    price = requests.get('https://coinbase.com/api/v1/prices/buy')
    return str(price.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
