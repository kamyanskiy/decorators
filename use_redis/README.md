# decorators

redis_cache_decorator.py - Decorator for class method that cashes values by unique user_id in Redis server.
 
Redis should be installed and running on machine, on Ubuntu:
$ apt-get install redis-server
 
$ cd use_redis
$ virtualenv -p python3.5 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

$ python test_redis_cache_decorator.py

$ ipython
```
>> from use_redis.redis_cache_decorator import UseRedisAsCache
>> instance = UseRedisAsCache('localhost', 6379)
>> instance.get_long_response(7)
>> Starting heavy calculations...
>> user id=7, some result: d6ddc2e91c6c48eabd7ebb529dd82308
>> Out[10]: 'd6ddc2e91c6c48eabd7ebb529dd82308'
>> instance.get_long_response(7)
>> FROM CACHE: user id=7, some result: d6ddc2e91c6c48eabd7ebb529dd82308
>> Out[11]: 'd6ddc2e91c6c48eabd7ebb529dd82308'

```