#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

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
    if username and username not in users:
        users[username] = {
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }
        return jsonify({"message": "User added", "user": users[username]}), 201
    else:
        return 400

if __name__ == "__main__":
    app.run()
