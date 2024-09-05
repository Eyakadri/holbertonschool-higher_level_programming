from flask import Flask, jsonify, request

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
        return jsonify({"error": "User not found"}), 404  # Return 404 if user not found


@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.json
    
    username = user_data.get('username')
    name = user_data.get('name')
    age = user_data.get('age')
    city = user_data.get('city')
    

if __name__ == "__main__":
    app.run()
