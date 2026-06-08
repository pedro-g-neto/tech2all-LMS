# Especificação de Requisitos - Tech2ALL

**Especificação do projeto das disciplinas Int. a Programação, Int. à Engenharia de Software e Programação Web I.**

**Alunos responsáveis: Pedro Gomes - João Freires - Emanuel Victor**

---

Estudantes de Engenharia de Software desejam desenvolver um sistema denominado Tech2ALL, com o objetivo de centralizar e organizar conteúdos educacionais gratuitos sobre tecnologia. O portal possuirá uma Landing Page (página inicial) contendo informações institucionais, apresentação dos benefícios da plataforma e botões de acesso para autenticação (Login e Cadastro).

A partir da área logada, o sistema disponibilizará um Catálogo Dinâmico onde serão exibidos os cursos agrupados por categorias (como Backend, Frontend, Dados). Ao clicar em um card de curso, o usuário acessará uma página de Detalhes do Curso. Para otimizar a performance e a arquitetura, o consumo do conteúdo em vídeo ocorrerá externamente. A página de detalhes fornecerá um link de redirecionamento direto para a playlist nativa do YouTube.

Para o gerenciamento individual de aprendizado, a página de detalhes do curso contará com uma To-Do List (Checklist) interativa contendo o cronograma de aulas. Após assistir a um vídeo externamente, o usuário deverá marcar a aula específica como concluída em seu painel. À medida que o aluno avança, o sistema calculará a porcentagem da barra de progresso. Toda a persistência de dados (usuários, cursos e status das aulas) será realizada em um Banco de Dados Relacional (SQLite) integrado via Flask-SQLAlchemy.

O portal também deverá disponibilizar uma página institucional sobre o projeto Tech2ALL, contendo informações sobre os desenvolvedores, o escopo da disciplina e as tecnologias utilizadas na implementação (HTML, CSS, Python e Flask). Outra funcionalidade esperada é uma página com o perfil do aluno, apresentando seus dados cadastrais básicos e um resumo geral informando quais cursos ele já iniciou e quais já foram finalizados dentro da plataforma.

O sistema deverá possuir dois perfis principais de acesso. O primeiro será o aluno autenticado, responsável principalmente por acessar as aulas, marcar vídeos como assistidos e gerenciar o seu próprio progresso. O segundo perfil será o administrador do sistema, responsável pela moderação do catálogo. O administrador poderá adicionar novos cursos e playlists do YouTube ou remover conteúdos desatualizados da plataforma.

### **1.  Stakeholders**

• **Usuário Final:** Pessoa interessada em consumir conteúdos de tecnologia.
• **Proprietário do Sistema:** Responsável por gerenciar o catálogo via CSV.

---

### **2. Requisitos Funcionais (RF)**

| ID | Requisito | Descrição |
| --- | --- | --- |
| RF01 | Autenticação | O sistema deve permitir que o usuário realize login para acessar a área de membros. |
| RF02 | Navegação por Temas e Landing Page | O sistema deve possuir uma página inicial pública (Landing Page) e uma rota protegida /catalogo que lista os cursos organizados por categorias. |
| RF03 | Visualização de Curso | O sistema deve permitir clicar em um card e abrir uma página detalhada com a descrição do curso e o botão de redirecionamento externo para o YouTube. |
| RF04 | Checklist de Aulas | O sistema deve exibir na página do curso uma lista de tarefas (To-Do list) com os nomes das aulas para acompanhamento manual. |
| RF05 | Controle de Progresso | O usuário deve poder marcar uma aula como "concluída". |
| RF06 | Persistência de Dados | O sistema deve salvar o catálogo, os usuários e o status de conclusão das aulas em um Banco de Dados relacional (SQLite). |
| RF07 | Contato e feedback | Página “Sobre” com o link do Github do projeto e os devidos créditos. |
| RF08 | Cadastro de Usuário | O sistema deve permitir que novos visitantes criem uma conta de acesso preenchendo um formulário com seus dados. |
| RF09 | Gerenciamento de Catálogo (Admin) | O sistema deve possuir uma rota restrita onde um administrador consiga adicionar novos cursos ao banco de dados via formulário e visualizar os cursos existentes em uma tabela. |
| RF10 | Feedback Visual (Sessões HTTP) | O sistema deve utilizar sessões para retornar notificações dinâmicas (mensagens de sucesso, erro ou alertas) após as ações do usuário. |
| RF11 | Perfil do Aluno | O sistema deve exibir uma página contendo os dados cadastrais do aluno logado e um resumo de quais cursos foram iniciados e finalizados. |
| RF12 | Tratamento de Exceções | O sistema deve validar as entradas de dados (como tentativa de login incorreto ou cadastro duplicado) e impedir operações inválidas, comunicando o erro de forma clara. |

### **3. Requisitos Não Funcionais (RNF)**

**3.1 Requisitos do Produto**
• **Usabilidade:** A interface deve ser responsiva, adaptando-se a Desktop e Mobile.
• **Eficiência:** O carregamento da lista de cursos a partir do CSV não deve demorar
• **Dependabilidade:** O sistema deve manter a integridade do arquivo CSV mesmo em caso de erro na escrita.

**3.2 Requisitos Organizacionais**
• **Desenvolvimento:** O sistema deve ser desenvolvido em Python 3.x com o framework Flask ****no backend, HTML e CSS no frontend e versionamento de código com Git
• **Padrões:** Os commits devem seguir o padrão *Conventional Commits*.

**3.3 Requisitos Externos**
• **Legislativos (LGPD):** O sistema não deve coletar dados sensíveis, utilizando apenas login básico e progresso acadêmico.

### **4. Casos de Uso e Estórias do Usuário**

**[UC01] Cadastro de Novo Usuário**

Como um visitante, eu quero criar uma conta na plataforma informando meus dados básicos, para que eu possa ter um perfil de estudante e realizar o login. (RF08/RF12)

Cenário 1: Cadastro realizado com sucesso

Dado que o visitante acessa a rota de cadastro (/cadastro)
Quando preenche o formulário com Nome, E-mail e Senha válidos
E clica no botão de registrar
Então o sistema deve salvar essas informações em uma nova linha na tabela de usuários do banco de dados
E redirecionar o usuário para a tela de login
E exibir uma mensagem flash de sucesso informando "Conta criada! Faça seu login".

Cenário 2: Tratamento de e-mail já existente

Dado que o visitante acessa a rota de cadastro
Quando preenche o formulário utilizando um e-mail que já consta no banco de dados
Então o sistema deve interromper a gravação
E recarregar a página de cadastro exibindo uma mensagem flash de erro informando "Este e-mail já está em uso".

**[UC02] Autenticação e Gestão de Sessão**

Como um usuário (Estudante ou Administrador), eu quero realizar login no sistema para acessar meu painel personalizado e manter meu progresso salvo de forma segura. (RF01/RF06/RF10/RF12)

Cenário 1: Login com sucesso
Dado que o usuário acessa a rota de login
Quando insere credenciais válidas e submete o formulário
Então o sistema deve iniciar uma sessão HTTP
E redirecionar o usuário para a página do catálogo dinâmico.

Cenário 2: Tratamento de erro no login
Dado que o usuário acessa a rota de login
Quando insere credenciais incorretas
Então o sistema deve retornar à página de login
E exibir uma mensagem flash de erro informando "Credenciais inválidas".

**UC03 - UC03 - Navegação na Landing Page e Acesso ao Catálogo**

Como um Estudante, eu quero visualizar cursos por categoria para encontrar o conteúdo de meu interesse. (RF02)

Dado que o estudante está devidamente autenticado.
Quando o estudante acessa a rota principal '/'.
Então o sistema deve ler o arquivo 'dados.csv'.
E exibir a tela inicial, utilizando laços de repetição para renderizar os cards dos cursos agrupados por categoria.
E exibir imagens de capa e links de navegação para as aulas.

**[UC04] Detalhes do Curso e Rastreamento de Progresso**

Como um Estudante, eu quero acessar os detalhes de um curso para obter o link da playlist e marcar manualmente as aulas assistidas em uma checklist, para manter meu progresso atualizado. (RF03/RF04/RF06)

Cenário 1: Redirecionamento e Atualização de progresso

Dado que o estudante acessa a página de detalhes de um curso específico

Quando clica no botão "Assistir no YouTube"

Então o sistema deve abrir a playlist em uma nova aba do navegador

E Quando o estudante marca o checkbox de uma aula na To-Do list

Então o sistema deve atualizar o campo concluida daquela aula no Banco de Dados

E a página deve recarregar exibindo a barra de progresso preenchida proporcionalmente.

**[UC05] Moderação de Catálogo (Painel Administrativo)**

Como um Administrador, eu quero acessar um painel restrito para adicionar novos cursos ao catálogo ou remover cursos antigos, garantindo que a plataforma esteja sempre atualizada. (RF09)

Cenário 1: Cadastro de novo curso

Dado que o administrador acessou o painel de controle
Quando preenche o formulário com Título, Categoria e Link do YouTube
E clica em salvar
Então o sistema deve anexar as informações em uma nova linha no banco de dados
E a tabela de listagem HTML na mesma página deve ser atualizada para exibir o novo curso.

**[UC06] Painel de Perfil do Aluno**

Como um aluno autenticado, eu quero acessar uma página de perfil dedicada para visualizar meus dados cadastrais e um resumo do meu desempenho, para saber rapidamente quantos cursos já iniciei e quantos já finalizei. (RF11)

Cenário 1: Visualização do resumo de progresso

Dado que o aluno está autenticado no sistema
Quando acessa a rota do seu perfil (/perfil)
Então o sistema deve ler os dados da sessão atual (Nome e E-mail)
E o sistema deve varrer o progresso do usuário filtrando pelo usuário logado
E exibir na tela a contagem total de cursos "Em Andamento" e cursos "Concluídos" (100%).

**[UC07] Página Institucional (Sobre)**

Como um visitante ou usuário da plataforma, eu quero acessar uma página institucional para conhecer o propósito do projeto Tech2ALL, as tecnologias utilizadas e a equipe desenvolvedora. (RF07)

Cenário 1: Acesso às informações do projeto

Dado que o usuário clica no link de navegação "Sobre"
Quando a página é carregada
Então o sistema deve exibir um texto explicativo sobre o escopo acadêmico do sistema
E exibir as badges das tecnologias (HTML, CSS, Python, Flask)
E listar os desenvolvedores responsáveis (Pedro Gomes, João Freires e Emanuel Victor) com links para seus respectivos perfis no GitHub.

---

### **5. Paleta de Cores do Projeto**

Background Principal (#131B2F): Azul-meia-noite

Superfícies e Cards (#1F2940): Um tom levemente mais claro que o fundo

Texto Principal (#E2E8F0): Cinza-claro

Ação e Destaque (#3B82F6): Azul vibrante para botões primários e links

Sucesso e Progresso (#10B981): Verde-esmeralda para a barra de progresso e feedbacks positivos

Erro e Alertas (#EF4444): Vermelho-suave
