from flask import Flask, request, jsonify

app = Flask(__name__)

variable = [0]

@app.route("/hello", methods=['GET'])
def hello_world():
    return jsonify("Hello, World!")

@app.route("/", methods=['GET'])
def hello_world1():
    return jsonify("Hello, World!")

@app.route("/example")
def print_variable():
    return variable


@app.route('/example', methods=['POST'])
def add_outcome():
    variable.append(request.get_json())
    return '', 204
# curl -X POST -H "Content-Type: application/json" -d "10" http://localhost:5000/example


@app.route("/sum")
def sumarize():
    sum=0
    for i in variable:
        print(i)
        sum += i
    return jsonify(sum), 200