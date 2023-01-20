#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB
printing out each request method in logs"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client["logs"]
    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for med in methods:
        criteria = {'method': med}
        print(
            "    method {}: {}".format(med, db.nginx.count_documents(criteria)))
    criteria = {'method': 'GET', 'path': '/status'}
    print("{} status check".format(db.nginx.count_documents(criteria)))
