from flask import Flask, jsonify, abort, request



app = Flask(__name__)

"""
api endpoint: /v1/helloWorld
returns  "Hello world"
"""
@app.route('/v1/helloWorld', methods=["GET"])
def get_hello_world():
    return jsonify("Hello, World"), 200

    """v1/double?1=5
    given url param
    should return {"value": "10"}
    """
@app.route('/v1/double/<int:value>', methods=['GET'])
def get_double_value(value):
    double = value * 2
    return jsonify({"value": str(double)})

    """[summary]

    Returns:
        json: get double, value by query param
    """
@app.route('/v1/double', methods=['GET'])
def get_double_param():
    if len(request.args) < 1:
        abort(400)
    elif request.args.get("i") == None:
        abort(400, "Value i not found")

    double = int(request.args.get("i")) * 2
    return jsonify({"value": str(double)})

if __name__ == "__main__":
    app.run(debug=True)

