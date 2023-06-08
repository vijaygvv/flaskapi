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



@app.route('/xlx')
def xlx():
    dataframe1 = pd.read_excel('login-data.xlsx')
    print(dataframe1)
    return ''


