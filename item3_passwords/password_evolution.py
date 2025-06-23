from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)
db_name = 'test.db'

def init_db():
    conn = sqlite3.connect(db_name)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/signup/v2', methods=['POST'])
def signup_v2():
    data = request.get_json()
    username = data['username']
    password = data['password']
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuario registrado con contraseña hasheada (v2)'})

@app.route('/login/v2', methods=['POST'])
def login_v2():
    data = request.get_json()
    username = data['username']
    password = data['password']
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password_hash))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({'message': 'Login exitoso (v2)'})
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5800, ssl_context='adhoc')