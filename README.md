# Redis + Python FastAPI

Projeto para integração e gerenciamento de dados com Redis e FastAPI.

## Configuração e Execução

### 1. Infraestrutura (Docker)
Para subir o banco de dados Redis e a interface visual Redis Insight:
```bash
docker-compose up -d
```

### 2. Variáveis de Ambiente
Configure as credenciais e endereços criando um arquivo .env com base no exemplo:
> Criar arquivo .env com base no .env.example

### 3. Scripts de Teste e Diagnóstico
Utilize os scripts abaixo para validar o ambiente:

* Testar a conexão com o Redis:
```bash
python test_redis.py
```

* Inserir dados de testes no Redis:
```bash
python test_populate_data.py
```

### 4. Interface Visual (Frontend)
Painel para visualização e gerenciamento dos dados:
* Redis Insight: http://localhost:5540/

### 5. Execução da API FastAPI
Para iniciar o servidor da aplicação:
```bash
uvicorn app:app --host 0.0.0.0 --port 5000
```
