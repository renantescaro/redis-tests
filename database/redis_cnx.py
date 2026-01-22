import os
from dotenv import load_dotenv
import redis.asyncio as redis
from fastapi import Request

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise Exception("Erro ao carregar 'REDIS_URL' das variaveis de ambiente!")

redis_pool = redis.ConnectionPool.from_url(REDIS_URL, decode_responses=True)


async def get_redis(request: Request):
    return request.app.state.redis
