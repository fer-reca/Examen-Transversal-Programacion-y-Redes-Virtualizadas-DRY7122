from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
PORT = 7500
DB_NAME = "usuarios.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE NOT NULL,
                hash_contrasena TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/registrar', methods=['POST'])
def registrar():
    datos = request.get_json()
    nombre = datos.get('nombre')
    contrasena = datos.get('contrasena')
    if not nombre or not contrasena:
        return jsonify({"error": "Faltan datos"}), 400
    hash_contrasena = generate_password_hash(contrasena)
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, hash_contrasena) VALUES (?, ?)', (nombre, hash_contrasena))
            conn.commit()
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Usuario ya existe"}), 409

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    nombre = datos.get('nombre')
    contrasena = datos.get('contrasena')
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT hash_contrasena FROM usuarios WHERE nombre = ?', (nombre,))
        fila = cursor.fetchone()
        if fila and check_password_hash(fila[0], contrasena):
            return jsonify({"mensaje": "Login exitoso"}), 200
        else:
            return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/', methods=['GET'])
def inicio():
    return "<h2>✅ Bienvenido a la API de Usuarios de DRY7122 S.A</h2><p>Usa Postman para /registrar y /login</p>"

if __name__ == '__main__':
    init_db()
    app.run(port=PORT)
