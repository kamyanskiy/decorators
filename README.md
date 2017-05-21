# decorators

simple_decorator.py - Simple decorator that uses dict to keep cached results per
 unique user_id

$ virtualenv -p python3.5 .venv
$ source .venv/bin/activate

$ python test_simple_decorator.py

$ python
```
>>> import simple_decorator
### First time value is calculated, written to cache
>>> simple_decorator.get_long_response(3)
>>> Out[6]: 3000
### Second time it returns from cache (by key from dict)
>>> simple_decorator.get_long_response(3)
>>> Out[6]: 3000
```
