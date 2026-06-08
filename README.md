# 🎓 Tech2ALL - Plataforma de Cursos em Vídeo

## 📖 Sobre o Projeto
Este projeto interdisciplinar foi desenvolvido para o 1º período de Engenharia de Software. Ele integra os conhecimentos das disciplinas de Programação Web 1, Introdução à Programação e Introdução à Engenharia de Software. O objetivo é criar uma aplicação web funcional, demonstrando a integração entre frontend e backend, além de aplicar práticas de gestão ágil e controle de versão.

O **Tech2ALL** é um Sistema de Gestão de Aprendizagem (LMS) simplificado onde os usuários podem acessar categorias de tecnologia, visualizar playlists de cursos do YouTube e acompanhar o próprio progresso marcando aulas concluídas.

## 🚀 Tecnologias Utilizadas
* **Frontend:** HTML5 Semântico, CSS3 (Design Responsivo), templates Jinja2.
* **Backend:** Python 3, Flask.
* **Armazenamento:** Persistência de dados baseada em banco de dados.
* **Gestão e Versionamento:** Git, GitHub (Projects, Issues, PRs seguindo o padrão *Conventional Commits*).
* **Modelagem:** Casos de Uso (draw.io) e BDD (Gherkin).

## ⚙️ Funcionalidades Principais (MVP)
* Catálogo dinâmico de cursos.
* Interface responsiva com formulários, tabelas de progresso e listas de módulos.
* Sistema de acompanhamento de progresso com sessões HTTP (Flask sessions).

## 👥 Equipe
Pedro Gomes de Andrade Neto

João Freires de Amorim Neto

Emanuel Victor Ribeiro Saturnino

## 📁 Estrutura do Projeto

LMS-project-ifpb/tech2all
 ├── app.py                # Arquivo principal de inicialização do Flask
 ├── instance/
 │   └── tech2all.db        # Banco de dados
 ├── static/
 │   ├── css/
 │   │   └── style.css     # Folhas de estilo da aplicação
 │   └── images/           # Imagens e logos
 ├── templates/
 │   ├── base.html         # Template base (layout padrão)
 │   ├── home.html        # Página inicial (Landing Page)
 │   └── detalhes.html         # Ambiente de visualização

├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto

## 🛠️ Como executar localmente
Clone o repositório:
git clone https://github.com/pedro-g-neto/LMS-project-ifpb.git


Acesse o diretório do projeto:
cd LMS-project-ifpb

Instale o Flask:
pip install flask flask-sqlalchemy

Acesse o diretório da aplicação:
cd tech2all

Execute a aplicação:
python app.py

Acesse no navegador: http://127.0.0.1:5000
