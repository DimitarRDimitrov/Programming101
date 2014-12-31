import unittest
import sql_manager


class TestUsers(unittest.TestCase):

    def test_injection():
        assertFalse(sql_manager.login("' OR 1 = 1 --", "any"))




if __name__ == '__main__':
    unittest.main()
