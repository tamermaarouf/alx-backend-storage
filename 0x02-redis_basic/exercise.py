#!/usr/bin/python3
'''Create a Cache class'''
import redis
import uuid


class Cache():
    '''method, store an instance of the Redis
    client as a private variable named _redis
    '''
    def __init__(self):
        self._redis = redis.Redis()

    def store(self, data:  Union[str, bytes, int, float]) -> str:
        '''store the input data in Redis
        using the random key and return the key.'''
        create_key = str(uuid.uuid4())
        self._redis.set(create_key, data)
        return (create_key)
