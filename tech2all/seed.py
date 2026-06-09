from app import app
from models import db, Curso

with app.app_context():


    # Instanciando os cursos
    curso1 = Curso(
        titulo="Python - Prof. Pietro", 
        categoria="Backend", 
        url_youtube="https://www.youtube.com/playlist?list=PLpaKFn4Q4GMN1A4J1FnhW_anOGt8ug8ip"
    )
    curso2 = Curso(
        titulo="Estrutura de Dados - Prof. Douglas Maioli", 
        categoria="Backend", 
        url_youtube="https://www.youtube.com/playlist?list=PLrOyM49ctTx_AMgNGQaic10qQJpTpXfn_"
    )
    curso3 = Curso(
        titulo="HTML e CSS - Otávio Miranda", 
        categoria="Frontend", 
        url_youtube="https://www.youtube.com/playlist?list=PLbIBj8vQhvm00J3f3rD33tRuNLem8EgEA"
    )
    curso4 = Curso(
        titulo="Machine Learning - Teo Me Why", 
        categoria="Dados", 
        url_youtube="https://www.youtube.com/playlist?list=PLvlkVRRKOYFR6_LmNcJliicNan2TYeFO2"
    )

    # Adiciona todos os objetos à sessão e commita no banco
    db.session.add_all([curso1, curso2, curso3, curso4])
    db.session.commit()

    print("Banco de dados populado com sucesso!")