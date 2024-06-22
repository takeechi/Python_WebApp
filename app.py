from flask import Flask
from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'
@app.route('/another')
def index():
    return 'Another Response'
@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'
@app.route('/exercise_request/<exercise_param>')
def exercise_request(exercise_param):
    return f'exercise_request:{exercise_param}'