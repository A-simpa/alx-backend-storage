#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB
printing out each request method in logs"""
from pymongo import MongoClient

client = MongoClient()
db = client["logs"]
print(f"{db.nginx.count_documents({})} logs")
print(f"Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for med in methods:
    print(f"\tmethod {med}: {db.nginx.count_documents({'method': med})}")
criteria = {'method': 'GET', 'path': '/status'}
print(f"{db.nginx.count_documents(criteria)} status check")
