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
    return 'name: categories'

@app.route('/question')
def question():
    return 'name: question'

@app.route('/answer')
def answer():
    return 'name: answer'

if __name__ == '__main__':
    app.run(debug=True)
