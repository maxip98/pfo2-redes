from flask import Flask, request, jsonify, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DATABASE = 'usuarios.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    contraseña_hash = generate_password_hash(contraseña)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)',
                           (usuario, contraseña_hash))
            conn.commit()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 409

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
        fila = cursor.fetchone()

        if fila and check_password_hash(fila[0], contraseña):
            return jsonify({'mensaje': f'Bienvenido, {usuario}'}), 200
        else:
            return jsonify({'error': 'Credenciales incorrectas'}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    html = '''
    <html>
    <head><title>Bienvenida</title></head>
    <body>
        <h1>Bienvenido al sistema de tareas</h1>
        <p>Por favor, acceda a sus tareas.</p>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
