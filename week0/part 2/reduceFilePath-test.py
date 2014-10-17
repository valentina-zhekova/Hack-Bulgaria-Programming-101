import unittest
from reduceFilePath import *


class ReduceFilePathTests(unittest.TestCase):
# return more than we have and don't start from root fail directory names
    def test_reduce_file_path_no_names_path(self):
        # as we start from root no-named directories can lead us only in root
        self.assertEqual("/", reduce_file_path("/"))
        self.assertEqual("/", reduce_file_path("//////////////"))
        self.assertEqual("/", reduce_file_path("/../"))

    def test_reduce_file_path_returns_more_than_we_can(self):
        # we can't escape root
        self.assertEqual("/", reduce_file_path("/aaa/bbb/../ccc/../../../"))

    # to throw "You haven't start from root!"???
    def test_reduce_file_path_returns_don_t_start_from_root(self):
        self.assertEqual(False, reduce_file_path("turtle/shrimps"))

    def test_reduce_file_path_accurate_instruction_moving(self):
        self.assertEqual("/", reduce_file_path("/srv/../"))
        self.assertEqual("/srv/www/htdocs/wtf",
                         reduce_file_path("/srv/www/htdocs/wtf/"))
        self.assertEqual("/srv/www/htdocs/wtf",
                         reduce_file_path("/srv/www/htdocs/wtf"))
        self.assertEqual("/srv", reduce_file_path("/srv/./././././"))
        self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))
        self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))

if __name__ == '__main__':
    unittest.main()

# тестовете трябва да са независими един от друг!
# def setUp(self) --> before all tests to avoid one kind initiallization
# def tearDown(self) --> after all tests ...
# тестовете не оставят следи, ако направим файл, трябва да го изтрием и т.н.
