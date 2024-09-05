from flask import Flask, jsonify, request

app = Flask(__name__)

# Initially an empty dictionary
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Return list of all usernames
@app.route('/data')
def get_users():
    print(f"Current users: {users}")  # Debugging info
    if not users:
        return jsonify([])  # Return empty list if no users exist
    return jsonify(list(users.keys()))

# Status endpoint
@app.route("/status")
def status():
    return "OK"

# Get user details by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    print(f"Received data: {request.json}")  # Debugging info

    # Check if request contains JSON
    if not request.is_json:
        return jsonify({"error": "Invalid data format, expected JSON"}), 400

    user_data = request.json

    # Validate user data
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Duplicate username"}), 400

    # Add user
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
