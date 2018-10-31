import os
from flask import Flask, render_template, g, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return 'hello world';

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port, debug=True)
    app.run(debug=True)
