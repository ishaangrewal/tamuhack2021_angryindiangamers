from flask import Flask, redirect, url_for, render_template, request
from tamuhack2021_angryindiangamers import script

app = Flask(__name__)

weight = None
height = None
age = None
sex = None
cholesterol = None
excercise = None
glucose = None
diastolic = None
systolic = None


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return "About"

@app.route("/predict/", methods=["POST", "GET"])
def predict():
    if request.method == "POST":

    else:
        render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)