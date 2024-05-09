"""
Web server application
Author: Ariba Siddiqi
1st May 2024
"""

from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
@app.route("/index.html")
def homepage():
    return render_template("./index.html")


@app.route("/about.html")
def aboutpage():
    return render_template("./about.html")


@app.route("/works.html")
def workspage():
    return render_template("./works.html")


@app.route("/contact.html")
def contactpage():
    return render_template("./contact.html")
