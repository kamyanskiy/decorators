import unittest

import simple_decorator as smd


class TestSimpleCacheDecorator(unittest.TestCase):
    def setUp(self):
        self.user_id = 5

    def test_cache_is_empty(self):
        self.assertTrue(smd.user_cache == {})

    def test_get_long_response_set_value_to_cache(self):
        expected = self.user_id*1000
        result = smd.get_long_response(self.user_id)
        self.assertTrue(result == expected)
        self.assertTrue(result == smd.user_cache.get(self.user_id))

    def test_get_long_response_writes_only_once_to_cache(self):
        result_1 = smd.get_long_response(self.user_id)
        result_2 = smd.get_long_response(self.user_id)
        self.assertTrue(result_1 == result_2)
        self.assertTrue(len(smd.user_cache.keys()) == 1)

    def test_get_long_response_uses_unique_user_id(self):
        another_user_id = 7
        smd.get_long_response(self.user_id)
        smd.get_long_response(another_user_id)
        smd.get_long_response(another_user_id)
        smd.get_long_response(self.user_id)

        # 4 calls, but 2 entries
        self.assertTrue(len(smd.user_cache.items()) == 2)

    def tearDown(self):
        smd.user_cache = {}

if __name__ == '__main__':
    unittest.main()
