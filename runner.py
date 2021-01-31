from flask import Flask, redirect, url_for, render_template, request
from tamuhack2021_angryindiangamers import script

app = Flask(__name__)

final = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/predict/", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        weight = request.form["weight"]
        height = request.form["height"]
        age = request.form["age"]
        sex = request.form["sex"]
        cholesterol = request.form["cholesterol"]
        glucose = request.form["gluc"]
        diastolic = request.form["diastolic"]
        systolic = request.form["systolic"]
        smoke = request.form["smoke"]
        alcohol = request.form["alch"]
        active = request.form["active"]
        global final
        final = [age, sex, height, weight, systolic, diastolic, cholesterol, glucose, smoke, alcohol, active]
        final = [float(x) for x in final]
        return redirect(url_for("predictions"))
    else:
        return render_template("predict.html")

@app.route("/predictions/")
def predictions():
    val = str(script.predict_cardiovscular(final))
    return render_template("prediction.html", val=val)

if __name__ == "__main__":
    app.run(debug=True)