from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"]

@app.route("/")
def index():
    price = fetch_bitcoin_price()
    return render_template("index.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)