from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Skyrim', 'RPG', 'PC')
jogo3 = Jogo('Fifa 24', 'Esporte', 'PS4')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():

    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo-jogo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar-jogo', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():

    if 'alohomora' == request.form['senha']:
        session['usuário logado'] = request.form['usuario']
        flash( session['usuário logado'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')

app.run(debug=True)
