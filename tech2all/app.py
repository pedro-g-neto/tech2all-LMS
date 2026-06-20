# app.py
from flask import Flask, render_template
from models import db, Curso

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

@app.route("/sobre")
def render_sobre():
    return render_template("sobre.html", current_user = MockUser())


if __name__ == '__main__':

    app.run(debug=True)