import redis
import asyncio


async def test():
    r = redis.asyncio.Redis(
        host="127.0.0.1",
        port=6379,
    )

    print(await r.ping())

    await r.close()


asyncio.run(test())