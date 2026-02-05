from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, OZ!"})

if __name__ == "__main__":
    app.run(debug=True, port=2000)