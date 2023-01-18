#!/usr/bin/env python3
"""list all document in my mongoDb collection"""


def list_all(mongo_collection):
    """list all document in  a mongodb collection"""
    return (mongo_collection.find())
