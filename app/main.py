import sqlite3
import os
import subprocess
import random
import jwt

# 💣 1. SQL Injection
def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '%s'" % user_id  # BAD
    cursor.execute(query)
    return cursor.fetchall()

# 💣 2. Hardcoded Secret
SECRET_KEY = "supersecret123"  # BAD

def encode_jwt(payload):
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# 💣 3. Insecure subprocess call (Command Injection)
def run_backup(file):
    subprocess.call("tar -czf /backup/" + file + ".tar.gz " + file, shell=True)  # BAD

# 💣 4. Insecure Random
def generate_token():
    return str(random.randint(100000, 999999))  # BAD

# 💣 5. Using eval()
def run_user_code(code):
    return eval(code)  # BAD

# 💣 6. Reading secrets from env but exposing them
def print_api_key():
    key = os.getenv("API_KEY")
    print("Using API Key:", key)  # BAD (exposing secret)
