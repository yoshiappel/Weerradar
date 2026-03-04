from urllib.request import urlopen
import json
from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)

url = "https://data.buienradar.nl/2.0/feed/json"

response = urlopen(url)

data = json.loads(response.read())

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get")
def get():
    return render_template("index.html", value="2 of 1")

@app.route("/3")
def userInput3():
    datum = data["forecast"]["weatherreport"]["published"]
    titel = data["forecast"]["weatherreport"]["title"]
    weerbericht = data["forecast"]["weatherreport"]["text"]
    author = data["forecast"]["weatherreport"]["author"]
    return render_template("index.html", datum=datum, titel=titel, weerbericht=weerbericht, author=author)

@app.errorhandler(404)
def redirect_to_root(e):
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)