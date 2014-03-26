from flask import Flask
import requests

app = Flask(__name__)
#app.debug = True

markup = 1.07

@app.route('/')
def hello_world():
    price = requests.get('https://coinbase.com/api/v1/prices/buy').json()['total']['amount']
    price = int(float(price))
    price = int(markup * price)
    return str(price)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
