import unittest
from memcache import Client

from cache_decorator import get_long_response


class TestCacheDecoratorWithMemcache(unittest.TestCase):
    def setUp(self):
        server = ["127.0.0.1:11211"]
        self.cache = Client(server)
        self.user_id = 5

    def test_cache_is_empty(self):
        value = self.cache.get(str(self.user_id))
        self.assertTrue(value is None)

    def test_get_long_response_set_value_to_cache(self):
        cached, result = get_long_response(self.user_id)
        self.assertTrue(cached is False)
        self.assertTrue(result == self.cache.get(str(self.user_id)))

    def test_get_long_response_gets_value_from_cache(self):
        cached_first_call, result_first_call = get_long_response(self.user_id)
        cached_second_call, result_second_call = get_long_response(self.user_id)
        self.assertTrue(cached_second_call is True)
        self.assertTrue(result_second_call == result_first_call)

    def test_get_long_response_uses_user_id_as_unique_key(self):
        another_user_id = 7

        cached_user1_1, result_user1_1 = get_long_response(self.user_id)
        cached_user1_2, result_user1_2 = get_long_response(self.user_id)

        cached_user2_1, result_user2_1 = get_long_response(another_user_id)
        cached_user2_2, result_user2_2 = get_long_response(another_user_id)

        self.assertTrue(cached_user1_2 is True)
        self.assertTrue(cached_user2_2 is True)

        self.assertTrue(result_user1_1 == result_user1_2)
        self.assertTrue(result_user2_1 == result_user2_2)

        self.assertFalse(result_user2_2 == result_user1_2)

        # remove entry in memcached.
        self.cache.delete(str(7))

    def test_delete_entry_in_cache_from_outside(self):
        cached, result = get_long_response(self.user_id)
        self.assertTrue(cached is False)

        value_in_cache = self.cache.get(str(self.user_id))
        self.assertTrue(result == value_in_cache)

        self.cache.delete(str(self.user_id))
        self.assertTrue(self.cache.get(str(self.user_id)) is None)

    def tearDown(self):
        self.cache.delete(str(self.user_id))
        self.cache.disconnect_all()


if __name__ == '__main__':
    unittest.main()
