import redis
from fastapi import APIRouter, Depends, HTTPException
from database.redis_cnx import get_redis

router = APIRouter()


@router.post("/set")
async def set_value(body: dict, db: redis.Redis = Depends(get_redis)):
    key = body.get("key")
    value = body.get("value")

    if not key or not value:
        return HTTPException(400)

    await db.set(key, value)
    return {"message": f"Chave {key} definida"}


@router.get("/get/{key}")
async def get_value(key: str, db: redis.Redis = Depends(get_redis)):
    result = await db.get(key)
    return {key: result}
