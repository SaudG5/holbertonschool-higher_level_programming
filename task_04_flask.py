#!/usr/bin/python3
"""A simple Flask API that stores users in memory."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return the welcome message of the API."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a JSON list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full user object for the given username, or a 404."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from the JSON body and return a confirmation."""
    user = request.get_json(silent=True)
    if not isinstance(user, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    username = user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
