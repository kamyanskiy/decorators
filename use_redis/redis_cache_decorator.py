import redis
from functools import wraps
from uuid import uuid4


redis_host = 'localhost'
redis_port = '6379'


def cache_method_decorator(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        id = args[0]
        if self.rds.exists(id):
            value = self.rds.get(id)
            print("FROM CACHE: user id={0}, some result: {1}".format(id,
                                                                     value))
            return value
        result = method(self, *args, **kwargs)
        self.rds.set(id, result)
        return result
    return wrapper


class UseRedisAsCache(object):

    def __init__(self, host, port):
        self.rds = redis.StrictRedis(host=host, port=port, db=0,
                                     decode_responses=True)

    @cache_method_decorator
    def get_long_response(self, user_id):
        print("Starting heavy calculations...")
        result = uuid4().hex
        print("user id={0}, some result: {1}".format(user_id, result))
        return result