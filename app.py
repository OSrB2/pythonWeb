from flask import Flask, render_template, request

app = Flask(__name__)

# POSTS MOCK
posts = [
  {
    'titulo': 'Post 1',
    'texto': 'Meu primeiro post.'
  },
  {
    'titulo': 'Post 2',
    'texto': 'Meu segundo post.'
  }
]

# USER MOCKS
USERNAME = 'admin'
PASSWORD = 'admin'

@app.route('/')
def exibir_entradas():
  return render_template('exibir_entradas.html', entradas=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  erro = ''
  if request.method == 'POST':
    if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
      return 'Usuário logado!'  
    erro = 'Usuário ou senha inválidos'
    
  return render_template('login.html', erro=erro)
