from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users storage
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        # Invalid JSON
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400

        # Missing username
        if "username" not in data or not data["username"]:
            return jsonify({"error": "Username is required"}), 400

        username = data["username"]

        # Duplicate username
        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        # Create user object
        user = {
            "username": username,
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }

        users[username] = user

        return jsonify({
            "message": "User added",
            "user": user
        }), 201

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run(debug=True)
