from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Carros, Usuarios

@app.route('/')
def index():
    lista = Carros.query.order_by(Carros.id)
    return render_template("index.html", titulo = 'carro', carro = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo= url_for('novo')))
    return render_template('novo.html', titulo='criar novo cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    
    marca = request.form['marca']
    modelo = request.form['modelo']
    ano = request.form['ano']
    cor = request.form['cor']
    preço = request.form['preço']
    placa = request.form['placa']

    #variavel nova recebendo classe jogo e filtrando pelo nome
    carro = Carros.query.filter_by(marca=marca).first()
    # if condicional recebendo a variavel caso exista jogos cadastrados 
    if carro:
        flash('Jogo Ja Existente!')
        return redirect(url_for('index'))

    #variavel criada recebendo variaveis e as variaveis refente ao form
    novo_carro = Carros(marca=marca, modelo=modelo, ano=ano, cor=cor, preço=preço, placa=placa)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(novo_carro)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    #redirecionamento para lista de jogos
    return redirect(url_for('index'))



@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo= url_for('editar')))
    #fazer uma query do banco
    carro = Carros.query.filter_by(id=id).first()
    return render_template('editar.html', titulo= 'Editar Jogo', carro = carro)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    pass



@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('voce foi Desconectado')

    return redirect(url_for('login'))

@app.route('/login')
def login():

        proximo = request.args.get('proximo')

        return render_template('login.html', proximo=proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():

    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + 'logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login'))