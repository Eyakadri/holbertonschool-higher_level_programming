from flask import Flask, jsonify, request

app = Flask(__name__)

# store users in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    return jsonify(list(users.keys()) if users else [])


@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify({"status": "success", "data": users[username]})
    return jsonify({"status": "error", "message": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
        
    username = data['username']
    users[username] = data
    
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)