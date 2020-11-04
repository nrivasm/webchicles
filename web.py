 #Grupo pablo
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "webchicles"

@app.route("/")
def home():
    return render_template("index.html", page="home")

@app.route("/About_Us/")
def aboutus():
    return render_template("aboutus.html", page="aboutus")

if __name__ == "__main__":
    app.run(debug=True)
