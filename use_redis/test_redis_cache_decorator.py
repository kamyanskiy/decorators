import unittest

from use_redis.redis_cache_decorator import UseRedisAsCache


class TestCacheDecoratorWithRedis(unittest.TestCase):
    def setUp(self):
        self.user_class = UseRedisAsCache('localhost', '6379')
        self.user_id = 5

    def test_cache_is_empty(self):
        value = self.user_class.rds.get(self.user_id)
        self.assertTrue(value is None)

    def test_get_long_response_set_value_to_cache(self):
        result = self.user_class.get_long_response(self.user_id)
        self.assertTrue(result == self.user_class.rds.get(self.user_id))

    def test_get_long_response_gets_value_from_cache(self):
        result_first_call = self.user_class.get_long_response(self.user_id)
        result_second_call = self.user_class.get_long_response(self.user_id)
        self.assertTrue(result_second_call == result_first_call)

    def tearDown(self):
        self.user_class.rds.delete(self.user_id)


if __name__ == '__main__':
    unittest.main()
