import json
import traceback
import base64
import logging
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senhaFib'
app.config['MYSQL_DATABASE_DB'] = 'fibdb'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql.init_app(app)

def Segundo():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%S')
    return int(data_e_hora_em_texto)

def teste():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from fibonacci")
    print cursor, str(cursor)
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    json_string = json.dumps(r, default=json_serial)
    print json_string
    return "Olá"

@app.route("/")
def hello():
    return "API Fibonacci!\n"

@app.route("/Teste")
def Teste():
    return "Welcome to teste!\n"

@app.route("/getDados")
def getDados():
    try:
        cursor = mysql.connect().cursor()
        
        vsql = "SELECT * from fibonacci where id = " + Segundo()
        
        cursor.execute(vsql)
        r = [dict((cursor.valor[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r, default=json_serial)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()

if __name__ == "__main__":
    #teste()
    app.run(host='0.0.0.0',debug=True)
