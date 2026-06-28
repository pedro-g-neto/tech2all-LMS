# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Curso, ProgressoUsuario, Usuario
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tech2all.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '$2a$12$ngQe9ooDjGtU57gaKxKCauCjaGDDx3YCHXb2mXZEQ9QKZiaXXaoZW' 


db.init_app(app)


with app.app_context():
    db.create_all()

# Mock temporário para evitar erros no Jinja2 do base.html
class MockUser:
    def __init__(self):
        self.is_admin = False

@app.route("/")
def home():
    usuario_falso = MockUser()
    return render_template('home.html', current_user=usuario_falso)


@app.route('/catalogo')
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
    
    usuario_falso = MockUser()

    return render_template('catalogo.html', cursos=lista_cursos, current_user=usuario_falso)

@app.route('/sobre')
def sobre():
    usuario_falso = MockUser()
    return render_template('sobre.html', current_user=usuario_falso)

# RENDERIZAR A PÁGINA COM A BARRA DE PROGRESSO
@app.route('/detalhes/<int:curso_id>')
def detalhes_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    
    usuario_falso = MockUser()
    # MOCK: Simulando o ID do usuário logado (depois trocar por current_user.id)
    usuario_id = 1 
    
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
                           porcentagem_conclusao=porcentagem_conclusao,
                           current_user=usuario_falso)

# RECEBER O CLIQUE DO CHECKBOX E SALVAR NO BANCO
@app.route('/detalhes/<int:curso_id>/atualizar-progresso', methods=['POST'])
def atualizar_progresso(curso_id):
    usuario_id = 1 # MOCK: ID do usuário logado
    
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

@app.route('/login')
def login():
    usuario_falso = MockUser()
    return render_template('login.html', current_user=usuario_falso)

@app.route('/cadastro')
def cadastro():
    usuario_falso = MockUser()
    return render_template('cadastro.html', current_user=usuario_falso)

if __name__ == '__main__':

    app.run(debug=True)