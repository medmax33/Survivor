import unittest
# import random
from level7_v1 import WordSearch


class MyTests(unittest.TestCase):

    phrase_1 = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'

    def test_in_example(self):
        self.assertEqual(WordSearch(12, self.phrase_1, 'строк'), [0, 0, 0, 1, 0, 0, 0])

    def test_12345(self):
        self.assertEqual(WordSearch(10, '12345', 'subs'), [0])

    def test_3_12345(self):
        self.assertEqual(WordSearch(3, '12345', '123'), [0, 0])


if __name__ == '__main__':
    unittest.main()
