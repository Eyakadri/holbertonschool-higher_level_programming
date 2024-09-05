from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username or username in users:
        return jsonify({"error": "Invalid or duplicate username"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()