import unittest

from unique_words_count import unique_words_count


class TestUniqueWords(unittest.TestCase):

    def test_zero_unique_words(self):
        self.assertEqual(0, unique_words_count([]))

    def test_one_unique_words(self):
        self.assertEqual(1, unique_words_count(["4u6ka"]))

    def test_morethanone_words(self):
        self.assertEqual(2, unique_words_count(["4u6ka", "zaek"]))

    def test_repeating_words_uniqueness(self):
        self.assertEqual(1, unique_words_count(["4u6ka", "4u6ka"]))

if __name__ == '__main__':
    unittest.main()
