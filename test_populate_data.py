import os
import redis
from dotenv import load_dotenv


def populate_test_data():
    try:
        load_dotenv()
        REDIS_URL = os.getenv("REDIS_URL")
        if not REDIS_URL:
            print("Erro ao carregar 'REDIS_URL' das variaveis de ambiente!")
            return

        r = redis.Redis.from_url(REDIS_URL)

        # teste de strings
        r.set("config:app_name", "MeuProjetoFastAPI")
        r.set("status:api", "online")

        # teste de hash (objetos)
        user_data = {"id": "1", "nome": "Teste", "email": "teste@exemplo.com"}
        r.hset("user:100", mapping=user_data)

        # teste de listas
        r.lpush("logs:access", "login_attempt", "page_view", "logout")

        print("Dados de teste inseridos com sucesso.")

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")


if __name__ == "__main__":
    populate_test_data()
