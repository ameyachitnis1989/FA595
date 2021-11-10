from Subjectivity import *
from nltk import text,FreqDist
import pandas as pd
from textblob import TextBlob
import webbrowser
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Main_pg():
    return '<h1>FA595 Mid Term Project</h1>\n<p><a href="/services">String Services</a></p>\n'


@app.route('/services')
def services():
    return '<h2>Services</h2><p><a href="/Subjectivity">Subjectivity</a></p>\n'

@app.route('/Subjectivity')
def Subjectivity():
    x='Ameya is a good boy'
    y=subjectivity(x)
    return render_template("Subjectivity.html",y=y)


if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True, port=5000)
