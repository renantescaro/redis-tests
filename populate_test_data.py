import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def populate_test_data():
    try:
        # teste de strings
        r.set("config:app_name", "MeuProjetoFastAPI")
        r.set("status:api", "online")

        # teste de Hash (objetos)
        user_data = {"id": "1", "nome": "Teste", "email": "teste@exemplo.com"}
        r.hset("user:100", mapping=user_data)

        # teste de Listas
        r.lpush("logs:access", "login_attempt", "page_view", "logout")

        print("Dados de teste inseridos com sucesso.")

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")


if __name__ == "__main__":
    populate_test_data()
