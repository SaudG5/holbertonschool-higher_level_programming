#!/usr/bin/python3
"""A Flask API secured with Basic authentication, JWT tokens and roles."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt, jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-this-to-a-long-random-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Return the username if the Basic auth credentials are valid."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message when valid Basic auth credentials are given."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Return a JWT access token when the JSON credentials are valid."""
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password or ""):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity=username,
                                additional_claims={"role": user["role"]})
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message when a valid JWT token is given."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return a message only when the JWT token belongs to an admin."""
    if get_jwt().get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Return 401 when the JWT token is missing."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Return 401 when the JWT token is invalid or malformed."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Return 401 when the JWT token has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Return 401 when the JWT token has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Return 401 when a fresh JWT token is required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
