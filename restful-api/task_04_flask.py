from flask import Flask, jsonify, request

app = Flask(__name__)

users = {} 

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    if not users:
        return jsonify([])
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
    user_data = request.json
    if not user_data:
        return jsonify({"error": "Invalid data"}), 400

    username = user_data.get("username")
    if not username or username in users:
        return jsonify({"error": "Invalid or duplicate username"}), 400

    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    })

if __name__ == "__main__":
    app.run()
