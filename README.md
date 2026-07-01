# 🎓 Tech2ALL - Plataforma de Cursos em Vídeo

## 📖 Sobre o Projeto
Este projeto interdisciplinar foi desenvolvido para o 1º período de Engenharia de Software. Ele integra os conhecimentos das disciplinas de Programação Web 1, Introdução à Programação e Introdução à Engenharia de Software. O objetivo é criar uma aplicação web funcional, demonstrando a integração entre frontend e backend, além de aplicar práticas de gestão ágil e controle de versão.

O **Tech2ALL** é um Sistema de Gestão de Aprendizagem (LMS) simplificado onde os usuários podem acessar categorias de tecnologia, visualizar playlists de cursos do YouTube e acompanhar o próprio progresso marcando aulas concluídas.

## Tecnologias Utilizadas
* **Frontend:** HTML5, CSS3, templates Jinja2.
* **Backend:** Python 3, Flask.
* **Armazenamento:** Persistência de dados baseada em banco de dados.
* **Gestão e Versionamento:** Git, GitHub (Projects, Issues).
* **Modelagem:** Casos de Uso (draw.io) e BDD (Gherkin).

## Funcionalidades Principais (MVP)
* Catálogo dinâmico de cursos.
* Interface responsiva com formulários, tabelas de progresso e listas de módulos.
* Sistema de acompanhamento de progresso com sessões HTTP (Flask sessions).

## Equipe
Pedro Gomes de Andrade Neto

João Freires de Amorim Neto

Emanuel Victor Ribeiro Saturnino

## Estrutura do Projeto

LMS-project-ifpb/tech2all
 ├── app.py                # Arquivo principal da aplicação

 ├── .env.example          # Arquivo exemplo para variáveis de ambiente

 ├── instance/

 │   └── tech2all.db        # Banco de dados

 ├── static/

 │   ├── css/

 │   │   ├── admin.css      # Folha de estilo do painel admin

 │   │   ├── auth.css       # Folha de estilo dos formulários de autenticação

 │   │   ├── catalogo.css   # Folha de estilo do catálogo de cursos

 │   │   ├── detalhes.css   # Folha de estilo da página de curso individual

 │   │   ├── home.css       # Folha de estilo da página inicial (Landing Page)

 │   │   ├── perfil.css     # Folha de estilo do perfil do usuário

 │   │   ├── sobre.css      # Folha de estilo do About

 │   │   └── style.css      # Folha de estilo da base

 │   └── images/           # Imagens e favicon

 ├── templates/

 │   ├── admin.html       # Painel administrativo  

 │   ├── base.html        # Template base 

 │   ├── cadastro.html    # Formulário de cadastro

 │   ├── catalogo.html    # Catálogo de cursos

 │   ├── detalhes.html    # Página de curso individual

 │   ├── home.html        # Página inicial (Landing Page)

 │   ├── login.html       # Formulário de Login

 │   ├── perfil.html      # Perfil do usuário

 │   └── sobre.html       # Sobre o projeto


├── .gitignore                     # Arquivos ignorados pelo Git

├── especificacao-requisitos.md    # Especificação de requisitos do projeto

└── README.md                      # Documentação do projeto


## 🛠️ Como executar localmente
Clone o repositório:
git clone https://github.com/pedro-g-neto/LMS-project-ifpb.git


Acesse o diretório do projeto:
cd LMS-project-ifpb

Crie e ative o ambiente virtual:

(Windows)

python -m venv venv

.\venv\Scripts\activate


(MAC/Linux)

python3 -m venv venv

source venv/bin/activate 


Instale as dependências:

pip install -r requirements.txt

Acesse o diretório da aplicação:

cd tech2all

Na raiz do projeto tech2all, localize o arquivo chamado .env.example.

Faça uma cópia deste arquivo e renomeie a cópia exatamente para .env.

Abra o arquivo .env e preencha a variável SECRET_KEY com uma string segura de sua preferência.

Execute a aplicação:

python app.py

Acesse no navegador: http://127.0.0.1:5000