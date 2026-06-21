from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TABELA DE USUÁRIOS
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# TABELA DE PROGRESSO
class ProgressoUsuario(db.Model):
    __tablename__ = 'progresso_usuario'
    id = db.Column(db.Integer, primary_key=True)
    
    # Relacionamentos
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    
    # Apenas o numero da aula que foi marcada
    aula_numero = db.Column(db.Integer, nullable=False)

class Curso(db.Model):
    __tablename__ = 'cursos'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    url_youtube = db.Column(db.String(255), nullable=False)
    url_capa = db.Column(db.String(255), nullable=True)
    qtd_aulas = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f'<Curso {self.titulo}>'
    
    