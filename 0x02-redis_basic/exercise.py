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


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        input_key = f'{key}:inputs'
        output_key = f'{key}:outputs'
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output = method(self, *args, **kwds)
        output_data = str(output)
        self._redis.rpush(output_key, output_data)
        return output
    return wrapper


def replay(method: Callable) -> None:
    ''' Check redis for how many times a function was called and display:
    How many times it was called
    Function args and output for each call
    '''
    key = method.__qualname__
    client = redis.Redis()
    input_key = f'{key}:inputs'
    output_key = f'{key}:outputs'
    input_data = [input.decode('utf-8') for input in
                  client.lrange(input_key, 0, -1)]
    output_data = [output.decode('utf-8') for output in
                   client.lrange(output_key, 0, -1)]
    call_count = client.get(key).decode('utf-8')
    print('{} was called {} times:'.format(key, call_count))
    for inputs, outputs in zip(input_data, output_data):
        print('{}(*{}) -> {}'.format(key, inputs, outputs))


class Cache():
    '''method, store an instance of the Redis
    client as a private variable named _redis
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
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
