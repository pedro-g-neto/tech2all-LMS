```
flowchart LR
    %% Atores
    V(["👤 Visitante"])
    A(["🎓 Aluno"])
    Admin(["⚙️ Administrador"])
    YT(["▶️ YouTube (Sistema)"])

    subgraph Tech2ALL [Tech2ALL]
        direction TB
        UC01(["UC01: Cadastrar Usuário"])
        UC02(["UC02: Realizar Login/Logout"])
        UC03(["UC03: Consultar Catálogo"])
        UC04(["UC04: Visualizar Detalhes e Playlist"])
        UC05(["UC05: Gerenciar Catálogo e Usuários"])
        UC06(["UC06: Consultar Perfil e Resumo"])
        UC07(["UC07: Visualizar Página 'Sobre'"])
        
        UC04Ext(["Marcar Progresso (Checklist)"])
        Validar(["Validar Credenciais"])
    end

    V --> UC01
    V --> UC07

    A -.->|Herda| V
    A --> UC02
    A --> UC03
    A --> UC04
    A --> UC06

    Admin -.-> |Herda| A
    Admin --> UC02
    Admin --> UC05

    
    UC04 -.->|interage| YT
    UC02 -.->|include| Validar
    UC04Ext -.->|extend| UC04

    style Tech2ALL fill:#131740,stroke:#3B82F6,stroke-width:2px,color:#E2E8F0
    style V fill:#131B2F,stroke:#fffff,color:#E2E8F0
    style A fill:#131B2F,stroke:#fffff,color:#E2E8F0
    style Admin fill:#131B2F,stroke:#fffff,color:#E2E8F0
    style YT fill:#EF4444,stroke:#fff,color:#fff
    ```