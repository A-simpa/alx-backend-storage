#!/usr/bin/env python3
"""defines the Cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """Defines a Cache class that initializes the database"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a data in a db"""
        key = str(uuid.uuid4)
        self._redis.set(key, data)
        return key
