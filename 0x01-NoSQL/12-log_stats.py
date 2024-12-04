#!/usr/bin/env python3
'''
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT","PATCH", "DELETE"]
'''


def log_stats():
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    print(db.nginx.count_documents({}))
    print(db)

