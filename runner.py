from flask import Flask, redirect, url_for, render_template
from tamuhack2021_angryindiangamers import script
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return "About"

@app.route("/predict/")
def predict():
    return "Predict"


if __name__ == "__main__":
    app.run(debug=True)