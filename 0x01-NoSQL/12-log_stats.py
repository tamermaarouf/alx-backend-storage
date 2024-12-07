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


def log_stats(nginx_collection):
    ''' Prints stats about Nginx request logs.
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    '''
    print("{} logs".format(nginx_collection.count_documents({})))
    print('Methods:')
    logs = nginx_collection.find({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    '''
    result = nginx_collection.aggregate(
            [{"$match": {"method":
             {"$in": ["GET", "POST", "PUT", "PATCH", "DELETE"] }}},
             { "$group": { "_id": "$method", "count": { "$sum": 1 } } },
             {"$sort" : {"count": -1}}])
    '''
    for word in methods:
        print("\tmethod {}: {}".format(
            word, (nginx_collection.count_documents({"method": word}))))
    print("{} status check".format(
        nginx_collection.count_documents({'method': 'GET', 'path': '/status'})))


def run():
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)


if __name__ == '__main__':
    run()
