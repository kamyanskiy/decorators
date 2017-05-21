from functools import wraps

# We will use dict structure as in memory cache
user_cache = {}


def cache_decorator(func):
    @wraps(func)
    def wrapper(arg):
        if user_cache.get(arg):
            value = user_cache.get(arg)
            return value
        result = func(arg)
        user_cache[arg] = result
        return result
    return wrapper


@cache_decorator
def get_long_response(user_id):
    return user_id*1000
