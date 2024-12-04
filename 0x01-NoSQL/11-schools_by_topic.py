#!/usr/bin/env python3
'''
Write a Python function that returns the list of school having a specific topic:
'''


def schools_by_topic(mongo_collection, topic):
    ''' return list of school'''
    # print(mongo_collection.find_one({"topics":topic}))
    return mongo_collection.find_one({"topics":topic})
