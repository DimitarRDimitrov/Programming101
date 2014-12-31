import unittest

from spam_and_eggs import prepare_meal


class Test_Spam_and_Eggs(unittest.TestCase):

    def test_eggs_only(self):
        self.assertEqual("eggs", prepare_meal(5))

    def test_one_spam(self):
        self.assertEqual("spam", prepare_meal(3))

    def test_two_spams(self):
        self.assertEqual("spam spam", prepare_meal(9))

    def test_no_meal_for_you(self):
        self.assertEqual("", prepare_meal(28))

    def test_two_spams_plus_eggs(self):
        self.assertEqual("spam spam and eggs", prepare_meal(45))


if __name__ == '__main__':
    unittest.main()
