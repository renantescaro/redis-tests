import os
import redis
import time
from dotenv import load_dotenv
from redis.exceptions import ConnectionError


def test_redis_connection():
    try:
        load_dotenv()
        REDIS_URL = os.getenv("REDIS_URL")
        if not REDIS_URL:
            print("Erro ao carregar 'REDIS_URL' das variaveis de ambiente!")
            return

        r = redis.Redis.from_url(REDIS_URL)

        # teste de ping
        start_ping = time.time()
        if r.ping():
            print(
                f"Conexão estabelecida! (Ping: {(time.time() - start_ping)*1000:.2f}ms)"
            )

        # teste de escrita
        r.set("teste_chave", "Olá Redis")
        print("Escrita de chave: OK")

        # teste de leitura
        valor = r.get("teste_chave")
        if valor == "Olá Redis":
            print(f"Leitura de chave: OK (Valor: {valor})")

        # teste de expiração
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
