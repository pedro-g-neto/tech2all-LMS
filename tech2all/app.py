# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Curso, ProgressoUsuario, Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
import csv
from datetime import datetime
from functools import wraps
from flask import abort

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tech2all.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '$2a$12$ngQe9ooDjGtU57gaKxKCauCjaGDDx3YCHXb2mXZEQ9QKZiaXXaoZW' 


db.init_app(app)

# CONFIGURAÇÃO DO FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Rota de login
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'error'

# Função que recarrega o usuário a cada requisição
@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(int(usuario_id))


with app.app_context():
    db.create_all()

# FUNÇÃO DE AUDITORIA
def registrar_log_csv(acao, email):
    # Salva o arquivo na mesma pasta do projeto
    caminho_arquivo = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'acessos_tech2all.csv')
    
    # Verifica se o arquivo já existe para decidir se precisa escrever o cabeçalho
    arquivo_existe = os.path.isfile(caminho_arquivo)
    
    # adiciona linhas no final do arquivo
    with open(caminho_arquivo, mode='a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        
        # Se for a primeira vez, cria as colunas
        if not arquivo_existe:
            escritor.writerow(['Data/Hora', 'Acao', 'Email_Usuario'])
            
        # Pega o horário do evento
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Escreve a nova linha de log
        escritor.writerow([agora, acao, email])

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('catalogo'))
    if request.method =='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        #Validação de email existente no banco
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('Este e-mail já está em uso. Tente fazer login.', 'error')
            return redirect(url_for('cadastro'))
        #Criação de usuário com senha criptografada
        senha_hash = generate_password_hash(senha)
        novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
        registrar_log_csv("NOVO_CADASTRO", email)
        flash('Conta criada com sucesso! Faça seu login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('cadastro.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('catalogo'))
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        #Busca usuário pelo e-mail
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            registrar_log_csv("LOGIN_REALIZADO", email)
            return redirect(url_for('catalogo'))
        else:
            flash('E-mail ou senha incorretos.', 'error')
            registrar_log_csv("FALHA_DE_LOGIN", email)
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    registrar_log_csv("LOGOUT", current_user.email)
    logout_user()
    return redirect(url_for('home'))

@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('catalogo'))
    return render_template('home.html')


@app.route('/catalogo')
@login_required
def catalogo():
    
    cursos_db = Curso.query.all()
    lista_cursos = [
        {
            'id': curso.id,
            'titulo': curso.titulo,
            'categoria': curso.categoria,
            'url_youtube': curso.url_youtube,
            'url_capa': curso.url_capa
        } for curso in cursos_db
    ]
    

    return render_template('catalogo.html', cursos=lista_cursos)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# RENDERIZAR A PÁGINA COM A BARRA DE PROGRESSO
@app.route('/detalhes/<int:curso_id>')
@login_required
def detalhes_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    
    usuario_id = current_user.id
    
    # Busca no banco quais números de aula este usuário já concluiu neste curso
    progressos = ProgressoUsuario.query.filter_by(usuario_id=usuario_id, curso_id=curso_id).all()
    
    # Transforma os objetos em uma lista para o Jinja ler
    aulas_concluidas = [p.aula_numero for p in progressos]
    
    # Calcula a porcentagem
    if curso.qtd_aulas > 0:
        porcentagem_conclusao = int((len(aulas_concluidas) / curso.qtd_aulas) * 100)
    else:
        porcentagem_conclusao = 0

    return render_template('detalhes.html', 
                           curso=curso, 
                           aulas_concluidas=aulas_concluidas,
                           porcentagem_conclusao=porcentagem_conclusao)

# RECEBER O CLIQUE DO CHECKBOX E SALVAR NO BANCO
@app.route('/detalhes/<int:curso_id>/atualizar-progresso', methods=['POST'])
@login_required
def atualizar_progresso(curso_id):
    #Pega o id de quem clicou no checkbox
    usuario_id = current_user.id
    
    # Limpa o progresso atual (para evitar duplicações ou aulas desmarcadas)
    ProgressoUsuario.query.filter_by(usuario_id=usuario_id, curso_id=curso_id).delete()
    
    # O request.form traz um dicionário só com as aulas marcadas
    for chave in request.form:
        if chave.startswith('aula_'):
            # Extrai o número da string "aula_3" -> 3
            numero_aula = int(chave.split('_')[1])
            
            # Cria o novo registro no banco
            novo_progresso = ProgressoUsuario(
                usuario_id=usuario_id,
                curso_id=curso_id,
                aula_numero=numero_aula
            )
            db.session.add(novo_progresso)
    
    # 3. Salva as alterações
    db.session.commit()
    
    # 4. Recarrega a página de detalhes para a barra de progresso atualizar visualmente
    return redirect(url_for('detalhes_curso', curso_id=curso_id))
# --- DECORADOR PARA PROTEGER ROTAS DE ADMIN ---
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Se não estiver logado ou não for admin, retorna erro 403 (Proibido)
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
@login_required
@admin_required
def painel_admin():
    cursos_db = Curso.query.all()
    usuarios_db = Usuario.query.all()

    return render_template('admin.html', cursos=cursos_db, usuarios=usuarios_db)

@app.route('/admin/novo', methods=['POST'])
@login_required
@admin_required
def admin_novo_curso():
    titulo = request.form.get('titulo')
    categoria = request.form.get('categoria')
    url_youtube = request.form.get('url_youtube')
    url_capa = request.form.get('url_capa')
    qtd_aulas = request.form.get('qtd_aulas', type=int)

    novo_curso = Curso(
        titulo=titulo,
        categoria=categoria,
        url_youtube=url_youtube,
        url_capa=url_capa,
        qtd_aulas=qtd_aulas
    )
    db.session.add(novo_curso)
    db.session.commit()

    flash('Curso adicionado com sucesso!', 'success')
    return redirect(url_for('painel_admin'))

@app.route('/admin/excluir/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_excluir_curso(id):
    curso = Curso.query.get_or_404(id)
    #Apagando o progresso dos alunos para não dar erro
    ProgressoUsuario.query.filter_by(curso_id=id).delete()

    db.session.delete(curso)
    db.session.commit()

    flash('Curso excluído com sucesso!', 'success')
    return redirect(url_for('painel_admin'))

@app.route('/admin/tornar-admin/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_promover_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if not usuario.is_admin:
        usuario.is_admin = True
        db.session.commit()
        flash(f'Agora {usuario.nome} é um administrador.', 'success')
    else:
        flash('Este usuário já é administrador.', 'info')
    return redirect(url_for('painel_admin'))


if __name__ == '__main__':

    app.run(debug=True)