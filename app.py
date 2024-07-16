from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'YOUR_COINMARKETCAP_API_KEY'  # Replace with your CoinMarketCap API key
API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

@app.route('/')
def home():
    response = requests.get(API_URL, headers=headers)
    data = response.json()
    cryptocurrencies = data['data'][:10]  # Get the top 10 cryptocurrencies
    return render_template('index.html', cryptocurrencies=cryptocurrencies)

if __name__ == '__main__':
    app.run(debug=True)
