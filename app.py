
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():


@app.route('/predict',method = 'POST')
def predict():

@app.route('/results',method='POST')
def results():
