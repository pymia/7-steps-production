from flask import Flask
from flask import request
from utils.prepare import load_model

app = Flask(__name__)
model = load_model("data/models/iris_model.pkl")


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/iris", methods=["GET"])
def predict():

    print(request.args)
    sepal_length = float(request.args.get("sepal_length"))
    sepal_width = float(request.args.get("sepal_width"))
    petal_length = float(request.args.get("petal_length"))
    petal_width = float(request.args.get("petal_width"))

    pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    response = {
        "input": [sepal_length, sepal_width, petal_length, petal_width],
        "pred": pred.tolist(),
    }
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
