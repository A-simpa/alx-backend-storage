#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB
printing out each request method in logs"""
from pymongo import MongoClient

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
