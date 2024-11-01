# API - Gerenciamento de Usuários, Contas e Transações

Bem-vindo ao projeto de API para gerenciamento de **usuários**, **contas bancárias** e **transações financeiras**. Este projeto foi desenvolvido com Django e Django Rest Framework.

---

## 🚀 Configuração do Ambiente

### 1. Criar um Ambiente Virtual
Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. No terminal, execute o seguinte comando para criar o ambiente:

```bash
python3 -m venv venv
2. Ativar o Ambiente Virtual
Após a criação, ative o ambiente virtual:

Linux/macOS:
source venv/bin/activate
Windows:
venv\Scripts\activate
3. Instalar Dependências
Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt
🗂️ Dependências Principais
As bibliotecas a seguir serão instaladas e são essenciais para o funcionamento da API:

Django==5.1.2 e djangorestframework==3.15.2: Componentes principais do framework para criação da API.
Dependências adicionais, como asgiref, sqlparse, tzdata, entre outras, para funcionalidades específicas e suporte ao projeto.
⚙️ Inicialização da API
1. Configuração do Projeto Django
Antes de iniciar o servidor, configure o banco de dados do projeto aplicando as migrações necessárias. No diretório do projeto, execute:

python manage.py migrate
2. Inicializar o Servidor de Desenvolvimento
Agora que o banco de dados está configurado, você pode iniciar o servidor de desenvolvimento. No diretório do projeto, execute:

python manage.py runserver
O servidor estará disponível em: http://127.0.0.1:8000/

🌟 Funcionalidades
Usuários: Registre novos usuários, obtenha tokens JWT para autenticação e gerencie detalhes de usuário.
Contas: Visualize e gerencie contas bancárias associadas a usuários.
Transações: Realize depósitos e saques com validação de saldo e acompanhe o histórico de transações.
📂 Estrutura do Projeto
A estrutura do projeto foi organizada para facilitar o desenvolvimento e a manutenção, com três principais aplicações:

project-root/
│
├── manage.py              # Script de gerenciamento do Django
├── requirements.txt       # Arquivo com as dependências do projeto
├── users/                 # Aplicação de gerenciamento de usuários
├── accounts/              # Aplicação para controle de contas bancárias
├── transactions/          # Aplicação para controle de transações financeiras
└── ...


principais rotas para gerenciar **usuários**, **contas** e **transações** em uma API. Abaixo estão os endpoints disponíveis e suas especificações.

## Base URL
http://localhost:8000

---

## Endpoints

### Users

- **Criar Usuário**

    - **URL**: `/api/user/`
    - **Método**: `POST`
    - **Headers**:
        - `Content-Type: application/json`
    - **Body**:
        ```json
        {
            "username": "teste12",
            "email": "senhacriptografada12@example.com",
            "password": "senha_segura"
        }
        ```

- **Ler Usuários**

    - **URL**: `/api/user/`
    - **Método**: `GET`

- **Obter Usuário por ID**

    - **URL**: `/api/user/{id}/`
    - **Método**: `GET`

- **Atualizar Usuário**

    - **URL**: `/api/user/{id}/`
    - **Método**: `PATCH`
    - **Headers**:
        - `Content-Type: application/json`
    - **Body**:
        ```json
        {
            "user": "novo_usuario",
            "email": "novo_email@example.com",
            "password": "nova_senha"
        }
        ```

- **Login**

    - **URL**: `/api/user/login/`
    - **Método**: `POST`
    - **Headers**:
        - `Content-Type: application/json`
    - **Body**:
        ```json
        {
            "username": "teste1",
            "password": "senha_segura"
        }
        ```

---

### Accounts

- **Ler Contas**

    - **URL**: `/api/account/`
    - **Método**: `GET`

- **Obter Conta por ID**

    - **URL**: `/api/account/{id}/`
    - **Método**: `GET`

---

### Transactions

- **Criar Transação**

    - **URL**: `/api/transaction/`
    - **Método**: `POST`
    - **Headers**:
        - `Content-Type: application/json`
    - **Body**:
        ```json
        {
            "account": 1,
            "amount": 50.00,
            "type": "saque"
        }
        ```

- **Ler Transações**

    - **URL**: `/api/transaction/`
    - **Método**: `GET`

- **Obter Transação por ID**

    - **URL**: `/api/transaction/{id}/`
    - **Método**: `GET`