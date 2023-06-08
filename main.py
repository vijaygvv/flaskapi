from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, Worldddddddd'



@app.route('/logdata')
def logdata():
    dataframe = pd.read_excel('data/login-data.xlsx')
    context = dataframe.to_json()
    return context



@app.route('/quarter')
def quarter():
    dataframe = pd.read_csv('data/march-quarter.csv')
    context = dataframe.to_json()
    return context

