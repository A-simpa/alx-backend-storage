#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB
printing out each request method in logs"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    db = client["logs"]
    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for med in methods:
        criteria = {'method': med}
        print(
            "\tmethod {}: {}".format(med, db.nginx.count_documents(criteria)))
    criteria = {'method': 'GET', 'path': '/status'}
    print("{} status check".format(db.nginx.count_documents(criteria)))

    mode_ips = db.nginx.aggregate([
        {"$match": {}},
        {"$project": {"ip": 1}},
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    print("IPs:")
    for ips in mode_ips:
        print("\t{}: {}".format(ips["_id"], ips["count"]))
