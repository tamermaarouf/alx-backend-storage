#!/usr/bin/env python3
'''
Write a Python script that provides
some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT","PATCH", "DELETE"]
'''
from pymongo import MongoClient


def log_stats():
    ''' Prints stats about Nginx request logs.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print("{} logs".format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for word in methods:
        print("\tmethod {}: {}".format(
            word, (nginx_collection.count_documents({"method": word}))))
    print("{} status check".format(nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'})))


if __name__ == '__main__':
    log_stats()
