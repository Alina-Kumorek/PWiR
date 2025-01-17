from flask import Flask, request, make_response, jsonify
import json
from calculator import experiment

app = Flask(__name__)

exper = experiment.Experiment(n=100, M=10, N=10)

@app.route("/")
def hello():
    return "Hello"

@app.route("/test")
def test():
    # return [{"x":1,"y":1}, {"x":2,"y":2}]
    return "test"

@app.route("/run", methods=['POST'])
def run_exp():
    if request.method == 'POST':

        data = request.form
        n=int(data["n"])
        M=int(data["m"])
        N=int(data["o"])

        exper = experiment.Experiment(n=n, M=M, N=N)
        exper.run()

        # exp.wyniki = [{"x":1,"y":1}, {"x":2,"y":2}]

        resp = make_response(jsonify(exper.wyniki))

        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        
        return resp
    else:
        return "You need to use POST method."

if __name__ == '__main__':
    app.run()