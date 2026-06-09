#Esse arquivo adiciona colunas a determinadas tabelas no banco de dados, não altere sem consultar o grupo
import sqlite3

def atualizar_banco():
    conexao = sqlite3.connect('instance/tech2all.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("ALTER TABLE cursos ADD COLUMN url_capa VARCHAR(255)")
        print("Coluna 'url_capa' criada com sucesso.")
    except sqlite3.OperationalError:
        print("A coluna 'url_capa' provavelmente já existe.")

    # 2. Atualiza as capas dos cursos
   # 2. Atualiza as capas dos cursos originais
    atualizacoes = [
        ("https://img.youtube.com/vi/wC_mwNUT48s/maxresdefault.jpg", 1),
        ("https://img.youtube.com/vi/-twvgnfOnVQ/maxresdefault.jpg", 2),
        ("https://img.youtube.com/vi/bCFTv8a59PE/maxresdefault.jpg", 3),
        ("https://img.youtube.com/vi/oz_rZ92Tmls/maxresdefault.jpg", 4)
    ]
    
    cursor.executemany("UPDATE cursos SET url_capa = ? WHERE id = ?", atualizacoes)
    conexao.commit()
    conexao.close()
    print("Capas atualizadas!")

if __name__ == '__main__':
    atualizar_banco()