import unittest
from countWords import count_words


class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1},
                         count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual({'ruby': 1, 'python': 3},
                         count_words(["python", "python", "python", "ruby"]))
        self.assertEqual({}, count_words([]))
# does it need to make difference between strings and numbers
# or everything is a word?

if __name__ == '__main__':
    unittest.main()
