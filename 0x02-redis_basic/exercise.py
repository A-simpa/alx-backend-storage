#!/usr/bin/env python3
"""defines the Cache class"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any, Optional


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, data):
        self._redis.incr(method.__qualname__, 1)
        return (method)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, args):
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        out = method(args, str)
        self._redis.rpush(method.__qualname__ + ":ouputs", out)
        return (method)
    return wrapper


class Cache:
    """Defines a Cache class that initializes the database"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a data in a db"""
        key = str(uuid.uuid4)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """get a data back using a callable fn"""
        val = self._redis.get(key)
        if fn is not None:
            return (fn(val))
        return val

    def get_str(self) -> Callable:
        """return string callable"""
        return (str)

    def get_int(self) -> Callable:
        """return int callable"""
        return (int)
