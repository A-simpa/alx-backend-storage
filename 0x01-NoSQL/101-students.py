#!/usr/bin/env python3
"""defines the top_students function"""


def top_students(mongo_collection):
    """returns all student sorted by average score"""
    docs = mongo_collection.aggregate([
        {"$match": {}},
        {"$unwind": "$topics"},
        {"$project": {
            "name": 1, "topics.score": 1}},
        {"$group": {"_id": "$_id",
                    "name": {"$first": "$name"},
                    "averageScore": {"$avg": {"$sum": "$topics.score"}}}},
        {"$sort": {"averageScore": -1}}
    ])
    return docs
