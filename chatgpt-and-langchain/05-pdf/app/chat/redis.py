import os
import redis

client = redis.Redis.from_url(
    os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    decode_responses=True,
)
