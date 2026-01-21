
Subir docker
docker-compose up -d

Script para testar a conexão com o Redis
python test_redis.py

Script para inserir dados de testes no Redis
python test_populate_data.py

Redis Insight - Frontend para vizualização dos dados do Redis 
http://localhost:5540/

Subir app FastAPI
uvicorn app:app --host 0.0.0.0 --port 5000
