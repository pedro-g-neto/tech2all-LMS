from app import app
from models import db, Usuario

with app.app_context():
    # Busca o seu usuário
    meu_user = Usuario.query.filter_by(email="pedro.neto.5@academico.ifpb.edu.br").first()
    
    # Altera a flag de admin para True
    meu_user.is_admin = True
    
    # Salva no banco
    db.session.commit()
    print("Promovido com sucesso!")