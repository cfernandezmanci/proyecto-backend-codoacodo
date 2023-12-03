from flask import Flask, request, jsonify, render_template
from flask import request
from flask_cors import CORS
from flask_mysqldb import MySQL
import mysql.connector
from werkzeug.utils import secure_filename


'''
Database host address:cacgrupo5.mysql.pythonanywhere-services.com
Username:cacgrupo5
Pass: Paste2023*
Database:  cacgrupo5$default
'''

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas
app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cacgrupo5'
app.config['MYSQL_PASSWORD'] = 'Paste2023*'
app.config['MYSQL_DB'] = 'cacgrupo5$default'

mysql = MySQL(app)

@app.route('/bebidas', methods=['GET'])
def handle_bebidas():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bebida")
        bebidas = cur.fetchall()
        cur.close()
        return jsonify(bebidas)

@app.route('/bebidas/<id>', methods=['GET'])
def handle_bebida(id):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bebida WHERE id = %s", [id])
        bebida = cur.fetchone()
        cur.close()
        return jsonify(bebida)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
