from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return "About"

@app.route("/predit/")
def predict():
    return "Predict"




if __name__ == "__main__":
    app.run()