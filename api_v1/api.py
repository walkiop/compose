#!/usr/bin/env python
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
app.config['MYSQL_DATABASE_DB'] = 'fibonaccidb'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql.init_app(app)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def Segundo():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%S')
    return data_e_hora_em_texto
    
@app.route("/")
def hello():
    return "Esta API gera números da sequencia de Fibonacci, pegando a posição conforme o segundo atual (getDados)!\n"

@app.route("/getDados")
def getDados():
    try:
        cursor = mysql.connect().cursor()
        sSql = "SELECT * from fibonacci where posicao = " + Segundo()
        cursor.execute(sSql)
        r = [dict((cursor.description[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r, default=json_serial)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()

if __name__ == "__main__":
    #teste()
    app.run(host='0.0.0.0',debug=True)
