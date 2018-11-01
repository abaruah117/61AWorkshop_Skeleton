import os
from flask import Flask, render_template, g, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'home'

@app.route('/categories')
def category():
    categories = requests.get('http://jservice.io/api/categories', {'count': 10})
    return categories.text

@app.route('/question')
def question():
    question = requests.get('http://jservice.io/api/random')
    return question.text

@app.route('/answer')
def check_answer():
    real_answer = 'Yes'
    input_answer = 'Yes'
    if real_answer.lower() == input_answer.lower():
        return 'Correct'
    else:
        return 'Incorrect'


if __name__ == '__main__':
    app.run(debug=True)
