"""
Web server application
Author: Ariba Siddiqi
1st May 2024
"""

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database_csv,
            delimiter=",",
            quotechar=" ",
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


@app.route("/")
def homepage():
    return render_template("./index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "something went wrong"
    else:
        return "re-try form submit"
