#!/usr/bin/env python3
'''Create a Cache class'''
import redis
import uuid
from typing import Any, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwds) -> Any:
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache():
    '''method, store an instance of the Redis
    client as a private variable named _redis
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store the input data in Redis
        using the random key and return the key.'''
        create_key = str(uuid.uuid4())
        self._redis.set(create_key, data)
        return (create_key)

    def get(self, key: str,
            fn: callable = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, lambda x: int(x))
