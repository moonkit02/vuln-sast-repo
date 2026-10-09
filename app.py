"""Intentionally vulnerable Flask app for SAST testing. Do not deploy."""
import hashlib
import os
import pickle
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

# Hardcoded secrets (fake) - triggers secret scanners
STRIPE_SECRET_KEY = "sk_demo_FAKE00abcdefghijklmnopqrstuvwxyz1234"
DB_PASSWORD = "SuperSecret123!"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user(username):
    # SQL injection: username concatenated straight into the query
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cur.execute(query)
    return cur.fetchall()

@app.route("/user")
def user_route():
    name = request.args.get("name", "")
    return str(get_user(name))

@app.route("/ping")
def ping():
    # OS command injection: host flows into a shell
    host = request.args.get("host", "")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output

@app.route("/load", methods=["POST"])
def load():
    # Insecure deserialization: untrusted pickle data
    data = request.get_data()
    return str(pickle.loads(data))

def hash_password(password):
    # Weak hashing: MD5, no salt
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    # Debug mode on in production-style entrypoint
    app.run(debug=True, host="0.0.0.0")
