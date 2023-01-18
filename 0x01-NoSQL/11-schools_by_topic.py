#!/usr/bin/env python3
"""list all document in my mongoDb collection by topics"""


def schools_by_topic(mongo_collection, topic):
    """list all document in  a mongodb collection by topics"""
    return (mongo_collection.find({"topics": topic}))
