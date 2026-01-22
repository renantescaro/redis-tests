import redis.asyncio as redis
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database.redis_cnx import redis_pool
from routes.manages_values import router as manages_values_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = redis.Redis(connection_pool=redis_pool)
    yield
    await app.state.redis.close()


app = FastAPI(lifespan=lifespan)
app.include_router(manages_values_router)
