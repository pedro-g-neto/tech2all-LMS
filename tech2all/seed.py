from app import app
from models import db, Curso

with app.app_context():


    # Instanciando os cursos de teste
    curso1 = Curso(
        titulo="Python Básico - Prof. Pietro", 
        categoria="Backend", 
        url_youtube="https://youtube.com/playlist?list=PLpaKFn4Q4GMN1A4J1FnhW_anOGt8ug8ip&si=sztrkQWLtkBxAIQ8",
        url_capa = "https://img.youtube.com/vi/wC_mwNUT48s/maxresdefault.jpg",
        qtd_aulas = 27
    )
    curso2 = Curso(
        titulo="HTML e CSS - Otávio Miranda", 
        categoria="Frontend", 
        url_youtube="https://youtube.com/playlist?list=PLbIBj8vQhvm00J3f3rD33tRuNLem8EgEA&si=MRUamhBTrjNDWX4I",
        url_capa = "https://img.youtube.com/vi/bCFTv8a59PE/maxresdefault.jpg",
        qtd_aulas = 45

    )
    curso3 = Curso(
        titulo="Machine Learning - Teo Me Why", 
        categoria="Dados", 
        url_youtube="https://youtube.com/playlist?list=PLvlkVRRKOYFR6_LmNcJliicNan2TYeFO2&si=p09L_D9rstI6gHsJ",
        url_capa = "https://img.youtube.com/vi/oz_rZ92Tmls/maxresdefault.jpg",
        qtd_aulas = 25
    )
    curso4 = Curso(
        titulo="Estruturas de Dados - Prof. Douglas Maioli", 
        categoria="Backend", 
        url_youtube="https://youtube.com/playlist?list=PLrOyM49ctTx_AMgNGQaic10qQJpTpXfn_&si=pur8VVxrwB1-rTzW",
        url_capa = "https://img.youtube.com/vi/-twvgnfOnVQ/maxresdefault.jpg",
        qtd_aulas = 34
    )
    curso5 = Curso(
        titulo = "Pandas: Manipulação de Dados - xavecoding",
        categoria = "Dados",
        url_youtube = "https://youtube.com/playlist?list=PL3ZslI15yo2pfkf7EGNR14xTwe-wZ2bNX&si=gAZK9Lt0e44gElDe",
        url_capa = "https://img.youtube.com/vi/hD0uJln4S2Y/maxresdefault.jpg",
        qtd_aulas = 27

    )

    # Adiciona todos os objetos à sessão e commita no banco
    db.session.add_all([curso1, curso2, curso3, curso4,curso5])
    db.session.commit()

    print("Banco de dados populado com sucesso!")