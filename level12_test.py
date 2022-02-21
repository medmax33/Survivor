import unittest
import random
from level12 import MassVote


class MyTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), 'majority winner 1')

    def test_zero(self):
        self.assertEqual(MassVote(3, [0, 0, 0]), 'no winner')

    def test_random(self):
        n = random.randint(1, 1000)
        votes = [101]
        for _ in range(1, n):
            votes.append(random.randint(1, 100))
        self.assertEqual(MassVote(n, votes), 'minority winner 1')


if __name__ == '__main__':
    unittest.main()
