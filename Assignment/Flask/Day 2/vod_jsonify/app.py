from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/v1/feeds", methods=["GET"])
def show_all_feeds():
    data = {}