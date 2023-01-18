#!/usr/bin/env python3
"""defines the insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """insert a document in a mongodb school collection"""
    return (mongo_collection.insert_one(kwargs).inserted_id)
