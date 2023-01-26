from flask import Flask, render_template, request, redirect, url_for, Response
import json
from infra.config.database import buscar, atualizaSitEmail, conectar, close, inserindoEmail, buscarsituacao
from infra.repositorios.repositoriosFuncs import validaCampo, validaCampoEmail, validaEmail, enviaremail
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {'db': "mysql+pymysql://root@localhost:3306/projeto_email"}
db = MongoEngine()
db.init_app(app)

class Item(db.Document):
    chave: int
    email: str
    assunto: str
    corpo: str




if __name__ == "__main__":
    app.run(debug=True, host='10.0.0.118', port='7000')
