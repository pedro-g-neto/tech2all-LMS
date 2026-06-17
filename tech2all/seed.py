from app import app
from models import db, Curso

with app.app_context():


    # Instanciando os cursos de teste
    curso1 = Curso(
        titulo="", 
        categoria="", 
        url_youtube="",
        url_capa = ""
    )
    curso2 = Curso(
        titulo="", 
        categoria="", 
        url_youtube="",
        url_capa = ""
    )
    curso3 = Curso(
        titulo="", 
        categoria="", 
        url_youtube="",
        url_capa = ""
    )
    curso4 = Curso(
        titulo="", 
        categoria="", 
        url_youtube="",
        url_capa = ""
    )

    # Adiciona todos os objetos à sessão e commita no banco
    db.session.add_all([curso1, curso2, curso3, curso4])
    db.session.commit()

    print("Banco de dados populado com sucesso!")