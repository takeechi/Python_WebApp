from flask import Flask, request, render_template, jsonify

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
@app.route('/show_html')
def show_html():
    return render_template('test_html.html')
@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')
@app.route('/exercise')
def exercise():
    my_name = request.args.get('my_name')
    return render_template('exercise_answer.html', name=my_name)

@app.route('/try_rest', methods=['POST'])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json":request_json}
    return jsonify(response_json)