from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Curso(db.Model):
    __tablename__ = 'cursos'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    url_youtube = db.Column(db.String(255), nullable=False)
    url_capa = db.Column(db.String(255), nullable=True)

    aulas = db.relationship('Aula', backref='curso_pai', lazy=True)

    def __repr__(self):
        return f'<Curso {self.titulo}>'
    
class Aula(db.Model):
    __tablename__ = 'aulas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    concluida = db.Column(db.Boolean, default=False)
    