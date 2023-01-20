from flask import Flask, render_template, request, redirect, url_for, Response
import json
from infra.config.database import buscar, atualizaSitEmail, conectar, close, inserindoEmail, buscarsituacao
from infra.repositorios.repositoriosFuncs import validaCampo, validaCampoEmail, validaEmail, enviaremail


app = Flask(__name__, template_folder="public")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validar', methods=['POST'])
def validaChave():
    if request.method == 'POST':
        result = request.form['chave']
        validar = buscar(result, "instituicao", "chave_toker")
        if validar == True:
            a = buscar(request.form['endereco'], "lista_email2", "email")
            if a != True:
                inserindoEmail(request.form['endereco'], "lista_email2", result)
            teste = validaEmail(request.form['endereco'])
            if teste == True: 
                if buscarsituacao(request.form['endereco'], "lista_email2", "email", 2) == False:
                    atualizaSitEmail("lista_email2", 2, request.form['endereco']) #para validos 
            else:
                if buscarsituacao(request.form['endereco'], "lista_email2", "email", 1) == False:
                    atualizaSitEmail("lista_email2", 1, request.form['endereco']) #para invalidos
            #enviar email
            if buscarsituacao(request.form['endereco'], "lista_email2", "email", 2) == True:
                enviaremail(request.form['assunto'], request.form['corpo'], request.form['endereco'])
                print("Email enviado!")
            else:
                print("Email não enviado!")
        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)