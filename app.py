from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
import redis.asyncio as redis

# Configuração do Pool
REDIS_URL = "redis://localhost:6379/0"
redis_pool = redis.ConnectionPool.from_url(REDIS_URL, decode_responses=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = redis.Redis(connection_pool=redis_pool)
    yield
    await app.state.redis.close()


app = FastAPI(lifespan=lifespan)


async def get_redis():
    return app.state.redis


@app.post("/set")
async def set_value(body: dict, db: redis.Redis = Depends(get_redis)):
    print(body)

    key = body.get("key")
    value = body.get("value")

    await db.set(key, value)
    return {"message": f"Chave {key} definida"}


@app.get("/get/{key}")
async def get_value(key: str, db: redis.Redis = Depends(get_redis)):
    result = await db.get(key)
    return {key: result}
