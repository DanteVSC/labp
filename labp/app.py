from flask import Flask, render_template, request, abort, jsonify,redirect,url_for
import math
from  model import Produto
app = Flask(__name__)


elemento = Produto()

@app.route('/conta', methods=['POST','GET'])
def conta():
     return render_template('conta.html')
#lista de produtos
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    if elemento.logar(nome,senha) == True:
        return redirect(url_for('conta'))
    
    elif elemento.logar(nome,senha) == False:
        return redirect(url_for('home'))
    
    elif elemento.logar(nome,senha) == 'cafetão':
        return redirect(url_for('abrir_admin'))

@app.route('/admin', methods=['POST','GET'])
def abrir_admin():
     return render_template('admin.html', produtos=elemento.get_produtos())

@app.route('/adicionar', methods=['POST','GET'])
def adicionar():
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    elemento.add(nome,preco)
    return redirect(url_for('abrir_admin'))

@app.route('/definir', methods=['POST','GET'])
def definir():
    id = request.form.get('id')
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    elemento.set_produto(id,nome,preco)
    return redirect(url_for('abrir_admin'))

@app.route('/deletar', methods=['POST','GET'])
def delete():
    id = request.form.get('id')    
    elemento.deletar(id)
    return redirect(url_for('abrir_admin'))


    #pega itens apenas da pagina atual
    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('produtos_paginados.html', produtos=produtos_da_pagina, page=page,total_pages=total_pages)

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto_encontrado = None

    for produto in PRODUTOS:
        if produto["id"] == produto_id:
             produto_encontrado = produto
             break
    if produto_encontrado is None:
        abort(404) 
    return render_template('detalhe_produto.html',produto=produto_encontrado)

@app.route('/api/buscar-produto',methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome').lower()

    resultado = [p for p in PRODUTOS if nome_produto in p['nome'].lower()]

    return jsonify({'produtos_encontrados':resultado})

if __name__ == '__main__':
        app.run(debug=True)