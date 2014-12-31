import unittest

from reduce_file_path import reduce_file_path


class TestReduceFilePath(unittest.TestCase):

    def test_edna_naklonena_4erta(self):
        self.assertEqual("/", reduce_file_path("/"))

    def test_rado_repository(self):
        self.assertEqual("/home/radorado/code/hackbulgaria",
                         reduce_file_path("//home//radorado/code/./hackbulgaria/week0/../"))

    def test_shrink_one(self):
        self.assertEqual("/", reduce_file_path("/srv/../"))

    def test_stay_in_srv(self):
        self.assertEqual("/srv", reduce_file_path("/srv/./././././"))

    def test_ingore_double_slash(self):
        self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))

    def test_multiple_reduce_to_root(self):
        self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))

    def test_only_slashes(self):
        self.assertEqual("/", reduce_file_path("//////////////////////"))

    def test_empty_path(self):
        # found error.. removed the first "/"
        self.assertEqual("/", reduce_file_path("/../"))


if __name__ == '__main__':
    unittest.main()
