from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    # TODO: index.html 반환
    return render_template("")


@app.route("/greet")
def greet():
    # TODO: URL에서 name 값 받아오기
    name = ??

    # TODO: greet.html 반환
    return render_template("", name=name)


if __name__ == "__main__":
    app.run(debug=True)