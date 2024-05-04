# Clouthes Back

**Clouthes Back** é um aplicativo backend desenvolvido com FastAPI para uma loja de roupas online. Ele oferece funcionalidades robustas para gerenciar usuários, autenticação, pedidos, produtos e devoluções.

## Recursos

- **Autenticação**: Sistema seguro de autenticação usando JWT.
- **Gestão de Produtos**: Visualização, criação e atualização de produtos.
- **Gestão de Pedidos**: Criação de pedidos e acompanhamento do status.
- **Gestão de Usuários**: Gerenciamento de contas de usuários e perfis.
- **Devoluções**: Solicitação e acompanhamento de devoluções.
- **CORS**: Configuração de CORS para permitir diferentes origens.

## Estrutura de Diretórios

```text
clouthes-back/
│
├── src/
│   ├── app.py              # Ponto de entrada principal
│   ├── config.py           # Configurações globais
│   │
│   ├── controllers/        # Controladores para as rotas
│   ├── database/           # Configuração do banco de dados
│   ├── middlewares/        # Middlewares para autenticação
│   ├── models/             # Modelos de dados
│   ├── routes/             # Definições de rotas
│   ├── services/           # Serviços para lógica de negócios
│   └── utils/              # Funções utilitárias
│
└── tests/                  # Testes unitários e de integração
```
## Requisitos

- Python 3.8+
- PostgreSQL

## Configuração do Projeto

1. **Clone o repositório**:

```
git clone <link_do_repositorio>
cd clouthes-back
```

2. **Crie e ative o ambiente virtual**:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

3. **Instale as dependências**:

```
pip install -r requirements.txt
```

4. **Configurar as variáveis de ambiente**:
Crie um arquivo .env na raiz do projeto com as configurações necessárias, por exemplo:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
JWT_SECRET_KEY=your-secret-key
```

5. **Iniciar o servidor**:
Use o comando uvicorn para iniciar o servidor:

```
uvicorn src.app:app --reload
```

6. **Acesse a documentação**:
Acesse a documentação interativa em http://localhost:8000/docs.

## Testes

Os testes estão localizados na pasta **'tests'**. Para executá-los, você pode usar **'pytest'**:

```
pytest
```

## Contribuição

1. Faça um fork do projeto.
2. Crie um branch para sua feature **(git checkout -b feature-xyz)**.
3. Faça commit das suas mudanças **(git commit -am 'Adiciona nova feature')**.
4. Envie para o branch **(git push origin feature-xyz)**.
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença **MIT** - veja o arquivo LICENSE para mais detalhes.