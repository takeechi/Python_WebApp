from flask import Flask, request, render_template, jsonify
from test_model_bk import Human
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)
engine = create_engine("sqlite:///test_db")
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
@app.route('/human_search')
def human_search():
    return render_template('human_search.html')
@app.route('/human_result')
def human_result():
    search_height = request.args.get("search_height")
    with Session(engine) as session:
        humans = session.query(Human).filter(Human.height > search_height)
    return render_template(
        "./human_result.html", humans=humans, search_height=search_height
    )
@app.route('/try_html')
def try_html():
    return render_template('try_html.html')
@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
    print(f'name: {request.form["name"]}')
    print(f'color: {request.form["color"]}')
    print(f'wether: {request.form["wether"]}')
    return render_template("try_html.html")

@app.route('/try_rest', methods=['POST'])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json":request_json}
    return jsonify(response_json)