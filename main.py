from flask import Flask,render_template, request, redirect, session, flash
from carro import Carro

carro1 = Carro("VW", "Gol", "2015","preto","35.000,00R$","HHH-5252")
carro2 = Carro("GM", "Corsa", "2008","Vermelho","18.000,00R$","BBB-0303")
carro3 = Carro("Toyota","Hilux","2020","branco","250.000,00R$","NNN-0202")
carro4 = Carro("Honda","Civic", "2022","rosa","230.000,00R$","MMM-1234")

lista = [carro1,carro2,carro3,carro4,]

app = Flask(__name__)
app.secret_key = '123456'

@app.route("/")
def inicio():
    return render_template('index.html', titulo = 'Home', carros = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = "Formulario de cadastro")


@app.route('/criar', methods=['POST'])
def criar():
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    ano = request.form["ano"]
    cor = request.form["cor"]
    preço = request.form["preço"]
    placa = request.form["placa"]

    carros = Carro(marca, modelo, ano, cor, preço, placa)

    lista.append(carros)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login Total ')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123456' == request.form['senha']:
        session['usuario_Logado'] = request.form['usuario']
        flash(session['usuario_Logado'] + 'Voce Esta Logado')
        return redirect("/")
    else:
        flash("Senha incorreta")
        return redirect('/login')
    
    
@app.route('/logout')   
def logout():
    session['usuario_Logado'] == None
    flash('Voce Foi Desconectado')
    return redirect('/login')


app.run(debug=True)
  