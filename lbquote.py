from flask import Flask, render_template
import requests
import decimal

app = Flask(__name__)
#app.debug = True

markup = 1.07
decimal.getcontext().prec = 4

@app.route('/')
def hello_world():
    price = requests.get('https://coinbase.com/api/v1/prices/buy').json()['total']['amount']
    price = int(float(price))
    price = int(markup * price)
    return str(price)

@app.route('/table')
def table():
    price = requests.get('https://coinbase.com/api/v1/prices/buy').json()['total']['amount']
    price = int(float(price))
    price = int(markup * price)
    pricetable = []
    for dollarvalue in [100,200,300,400,500,1000,2000]:
        pricetable.append('$%s for %s BTC' % (dollarvalue, decimal.Decimal(dollarvalue)/price))
    return render_template('quote.html', pricetable=pricetable)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
