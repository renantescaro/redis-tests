import redis
import time
from redis.exceptions import ConnectionError


def test_redis_connection():
    try:
        r = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
            socket_connect_timeout=5,
            decode_responses=True,
        )

        # teste de Ping
        start_ping = time.time()
        if r.ping():
            print(
                f"Conexão estabelecida! (Ping: {(time.time() - start_ping)*1000:.2f}ms)"
            )

        # teste de Escrita
        r.set("teste_chave", "Olá Redis")
        print("Escrita de chave: OK")

        # teste de Leitura
        valor = r.get("teste_chave")
        if valor == "Olá Redis":
            print(f"Leitura de chave: OK (Valor: {valor})")

        # teste de Expiração
        r.setex("chave_temporaria", 2, "vou sumir")
        print("Teste de TTL (2s) iniciado...")
        time.sleep(2.5)
        if r.get("chave_temporaria") is None:
            print("Expiração de chave: OK")

    except ConnectionError as e:
        print(f"Erro de Conexão: Verifique se o container está rodando.\nDetalhes: {e}")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    test_redis_connection()
