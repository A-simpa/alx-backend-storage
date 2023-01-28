#!/usr/bin/env python3
"""implement web page cache"""
import requests
import redis


def get_page(url: str) -> str:
    """request a page"""
    db = redis.Redis()
    db.incr("count:{}".format(url), 1)
    db.expireat("count:{}".format(url), 10)
    x = requests.get(url)
    return (x.text)
