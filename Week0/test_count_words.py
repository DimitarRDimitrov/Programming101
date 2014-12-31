import unittest

from count_words import count_words


class CountWordsTest(unittest.TestCase):

    # def test_if_word_present_in_mydict(self):
    #     count_words(["kaluf"])
    #     self.assertIn("kaluf", count_words.my_dict)

    def test_if_word_is_added(self):
        self.assertEqual({'kaluf': 1}, count_words(["kaluf"]))

    def test_if_word_second_added(self):
        self.assertEqual({'kaluf': 2}, count_words(["kaluf", "kaluf"]))

    def test_two_words_if_added(self):
        self.assertEqual(
            {'kaluf': 1, "4u6ka": 1}, count_words(["kaluf", "4u6ka"]))

    def test_zero_dictionary(self):
        self.assertEqual({}, count_words([]))


if __name__ == '__main__':
    unittest.main()
