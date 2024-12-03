#!/usr/bin/env python3
'''Write a Python function that inserts a new document in a collection based on kwargs:'''


def insert_school(mongo_collection, **kwargs):
    '''Returns the new _id'''
    for key,value in kwargs.items():
        new_id = mongo_collection.insert_one(dict({key:value}))
    return new_id
