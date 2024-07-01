from flask import Flask, request, jsonify
import sqlite3
import bcrypt

app = Flask(__name__)

# Inicializar la base de datos SQLite
def initdb():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Llamar función para inicializar la base de datos
initdb()

# Función para agregar usuario inicial (jorge - 12345)
def agregarusuarioinicial():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    # Verificar si el usuario ya existe
    cursor.execute('SELECT * FROM usuarios WHERE nombre=?', ('jorge',))
    usuario = cursor.fetchone()
    if not usuario:
        # Si no existe, agregar usuario inicial
        password = '12345'
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute('INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)', ('jorge', password_hash))
        conn.commit()
    conn.close()

# Llamar función para agregar usuario inicial
agregarusuarioinicial()

# Ruta para validar usuarios
@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['nombre']
    password = request.form['password']

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM usuarios WHERE nombre = ?', (nombre,))
    row = cursor.fetchone()
    conn.close()

    if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
        return jsonify({"message": "Login exitoso"})
    else:
        return jsonify({"message": "Nombre o contraseña incorrectos"}), 401

if __name__ == "__main__":
    app.run(port=8500)
