from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/user/<name>")
def hello_json(name):
    return jsonify(message=f"{name}님, BE 캠프에 오신 걸 환영합니다!")

if __name__ == "__main__":
    app.run(debug=True, port=2000)