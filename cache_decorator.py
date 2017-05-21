from functools import wraps
from uuid import uuid4

from memcache import Client

servers = ["127.0.0.1:11211"]
user_cache = Client(servers)


def cache_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = args[0]
        if user_cache.get(str(id)):
            value = user_cache.get(str(id))
            print("FROM CACHE: user id={0}, some result: {1}".format(str(id),
                                                                     value))
            return True, value
        result = func(*args, **kwargs)
        user_cache.set(str(id), result)
        return False, result
    return wrapper


@cache_decorator
def get_long_response(user_id):
    print("Starting heavy calculations...")
    result = uuid4().hex
    print("user id={0}, some result: {1}".format(user_id, result))
    return result
