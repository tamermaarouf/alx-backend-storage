#!/usr/bin/env python3
'''Write a Python function that inserts a new document in a collection based on kwargs:'''


def insert_school(mongo_collection, **kwargs):
    '''Returns the new _id'''
    new_insert = {}
    for key,value in kwargs.items():
        new_insert[key] = value
    return mongo_collection.insert_one(new_insert)
