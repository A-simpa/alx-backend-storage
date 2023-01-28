#!/usr/bin/env python3
"""implement web page cache"""
from typing import Callable
import requests
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """wrapper to count how many times a function is called"""
    @wraps(method)
    def wrapper(url):
        db = redis.Redis()
        db.incr("count:{}".format(url), 1)
        db.expireat("count:{}".format(url), 10)
        return method(url)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """request a page"""
    db = redis.Redis()
    x = requests.get(url)
    return (x.text)
