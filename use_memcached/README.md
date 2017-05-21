# decorators

cache_decorator.py - Decorator that cashes values by unique user_id in memcached server.
 
memcached should be installed and running on machine, on Ubuntu:
$ apt-get install memcached
 
$ cd use_memcached
$ virtualenv -p python3.5 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

$ python test_cache_decorator.py

$ ipython

>>> In [1]: import cache_decorator
### First time value is calculated, written to cache
>>> In [2]: cache_decorator.get_long_response(44)
>>> Starting heavy calculations...
>>> user id=44, some result: 708245a5872742c38a77e07847f583f4
>>> Out[2]: (False, '708245a5872742c38a77e07847f583f4')
### Second time it returns from cache (by key from memcached)
>>> In [3]: cache_decorator.get_long_response(44)
>>> FROM CACHE: user id=44, some result: 708245a5872742c38a77e07847f583f4
>>> Out[3]: (True, '708245a5872742c38a77e07847f583f4')
