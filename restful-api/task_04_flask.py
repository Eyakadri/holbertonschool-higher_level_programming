from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

# In-memory user storage
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))  # Return list of usernames

@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404  # Return 404 if user not found

if __name__ == "__main__":
    app.run()
