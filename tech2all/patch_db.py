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
    atualizacoes = [
        ("https://i.ytimg.com/vi/wC_mwNUT48s/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBpep7ian3cwG7_0y9m6FyYe1WamA", 1),
        ("https://i.ytimg.com/vi/-twvgnfOnVQ/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD-B47XrbnHf29yQ5RzGGUXMyH9DQ", 2),
        ("https://i.ytimg.com/vi/bCFTv8a59PE/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD_9yoL6lokKr68f1M-r4PlMEUSYA", 3),
        ("https://i.ytimg.com/vi/oz_rZ92Tmls/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBdB87Vzx_0G9P1AOjmIT_g9bgWIg", 4)
    ]
    
    cursor.executemany("UPDATE cursos SET url_capa = ? WHERE id = ?", atualizacoes)
    conexao.commit()
    conexao.close()
    print("Capas atualizadas!")

if __name__ == '__main__':
    atualizar_banco()