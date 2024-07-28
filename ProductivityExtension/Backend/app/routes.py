from flask import Flask, redirect, render_template, request, session, jsonify, Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=['GET', 'POST'])
def index():
  return render_template("home.html")


@main_bp.route("/data", methods=['GET'])
def get_data():
  data = {
    "seconds": 21
  }
  
  return jsonify(data)


# if __name__ == '__main__':
#     app.run(debug=True)