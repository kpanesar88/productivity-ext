from flask import Flask, redirect, render_template, request, session, jsonify


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/data")
def get_data():
  data = {
    "seconds": 0
  }
  
  return jsonify(data)