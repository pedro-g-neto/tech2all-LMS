# Especificação de Requisitos - Tech2ALL

**Especificação do projeto das disciplinas Int. a Programação, Int. à Engenharia de Software e Programação Web I.**

**Alunos responsáveis: Pedro Gomes - João Freires - Emanuel Victor**

---

Estudantes de Engenharia de Software desejam desenvolver um sistema denominado Tech2ALL, com o objetivo de centralizar e organizar conteúdos educacionais gratuitos sobre tecnologia disponíveis no YouTube, além de permitir o acompanhamento contínuo do progresso de estudo dos alunos. O portal deverá possuir uma página inicial contendo o catálogo de cursos da plataforma, além de acesso às principais funcionalidades do sistema. Nessa página deverão ser exibidos os cursos disponíveis agrupados por categorias (como Backend, Frontend, Dados) e subcategorias (como Java, Go, Python, Análise de Dados e Web Scraping), apresentando cards personalizados para cada playlist do YouTube, além de links de navegação.

O sistema deverá permitir o gerenciamento individual de aprendizado. Usuários autenticados poderão clicar em um card de curso para acessar uma aba dedicada de reprodução. Nessa aba, será exibido o player de vídeo nativo do YouTube e uma lista com o cronograma de aulas do curso. Após assistir a um vídeo, o usuário poderá marcar aquela aula específica como concluída em seu painel.

À medida que o aluno avança, o sistema deverá processar essa confirmação. Quanto mais aulas forem marcadas como concluídas, maior deverá ser a porcentagem preenchida na barra de progresso daquele curso exibida pelo sistema, avançando até completar 100%. Além disso, o portal deverá salvar o status de todas as aulas no banco de dados local (arquivo CSV), permitindo que os alunos consultem os cursos em andamento a qualquer momento. A visualização do catálogo e a área de cadastro e login devem ser acessadas a partir da página principal.

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
| RF02 | Navegação por Temas | A página inicial deve listar cursos organizados por categorias (Backend, Frontend, Dados, etc.). |
| RF03 | Visualização de Curso | O sistema deve permitir clicar em um card de curso e abrir a página de reprodução. |
| RF04 | Reprodução de Vídeo | O sistema deve exibir o player do YouTube (iframe) e a lista de aulas da playlist. |
| RF05 | Controle de Progresso | O usuário deve poder marcar uma aula como "concluída". |
| RF06 | Persistência de Dados | O sistema deve salvar o status de conclusão de cada aula no arquivo `dados.csv`. |
| RF07 | Contato e feedback | Página “Sobre” com o link do Github do projeto e os devidos créditos. |
| RF08 | Cadastro de Usuário | O sistema deve permitir que novos visitantes criem uma conta de acesso preenchendo um formulário com seus dados. |
| RF09 | Gerenciamento de Catálogo (Admin) | O sistema deve possuir uma rota restrita onde um administrador consiga adicionar novos cursos ao CSV via formulário e visualizar os cursos existentes em uma tabela. |
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
Então o sistema deve salvar essas informações em uma nova linha no arquivo de persistência (ex: `usuarios.csv`)
E redirecionar o usuário para a tela de login
E exibir uma mensagem flash de sucesso informando "Conta criada! Faça seu login".

Cenário 2: Tratamento de e-mail já existente

Dado que o visitante acessa a rota de cadastro
Quando preenche o formulário utilizando um e-mail que já consta no arquivo CSV
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

**UC03 - Navegação por Temas e Catálogo de Cursos**

Como um Estudante, eu quero visualizar cursos por categoria para encontrar o conteúdo de meu interesse. (RF02)

Dado que o estudante está devidamente autenticado.
Quando o estudante acessa a rota principal '/'.
Então o sistema deve ler o arquivo '`dados.csv`'.
E exibir a tela inicial, utilizando laços de repetição para renderizar os cards dos cursos agrupados por categoria. E exibir imagens de capa e links de navegação para as aulas.

**[UC04] Player de Aula e Rastreamento de Progresso**

Como um Estudante, eu quero acessar uma aba dedicada com o vídeo do curso e poder marcar as aulas como concluídas, para que o sistema calcule a barra do meu progresso. (RF04/RF05/RF06)

Cenário 1: Atualização de progresso

Dado que o estudante está na página de reprodução de um curso
E a barra de progresso atual exibe "0%"
Quando o estudante clica no botão "Marcar Aula como Concluída"
Então o sistema deve atualizar o status daquela aula no arquivo `dados.csv`
E o sistema deve recalcular matematicamente o avanço
E a página deve recarregar exibindo a barra de progresso preenchida proporcionalmente.

**[UC05] Moderação de Catálogo (Painel Administrativo)**

Como um Administrador, eu quero acessar um painel restrito para adicionar novos cursos ao catálogo ou remover cursos antigos, garantindo que a plataforma esteja sempre atualizada. (RF09)

Cenário 1: Cadastro de novo curso

Dado que o administrador acessou o painel de controle
Quando preenche o formulário com Título, Categoria e Link do YouTube
E clica em salvar
Então o sistema deve anexar as informações em uma nova linha no arquivo `dados.csv`
E a tabela de listagem HTML na mesma página deve ser atualizada para exibir o novo curso.

**[UC06] Painel de Perfil do Aluno**

Como um aluno autenticado, eu quero acessar uma página de perfil dedicada para visualizar meus dados cadastrais e um resumo do meu desempenho, para saber rapidamente quantos cursos já iniciei e quantos já finalizei. (RF11)

Cenário 1: Visualização do resumo de progresso

Dado que o aluno está autenticado no sistema
Quando acessa a rota do seu perfil (/perfil)
Então o sistema deve ler os dados da sessão atual (Nome e E-mail)
E o sistema deve varrer o arquivo de progresso (`dados.csv`) filtrando pelo usuário logado
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
