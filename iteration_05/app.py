from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template("contact.html", email=" ")

@app.route("/about")
def about():
    return render_template("about.html", author=" ")

app.run(debug=True)