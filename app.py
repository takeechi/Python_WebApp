from flask import Flask

app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'
@app.route('/another')
def index():
    return 'Another Response'