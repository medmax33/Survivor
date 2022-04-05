import unittest
from level24 import MatrixTurn


class MyTests(unittest.TestCase):

    def test_2x2_1t(self):
        self.mmm = ['12','34']
        MatrixTurn(self.mmm, 2, 2, 1)
        self.assertEqual(self.mmm, ['31', '42'])

    def test_2x2_3t(self):
        self.mmm = ['12','34']
        MatrixTurn(self.mmm, 2, 2, 3)
        self.assertEqual(self.mmm, ['24', '13'])

    def test_4x6_1t(self):
        self.mmm = ['123456','345678','567890','890123']
        MatrixTurn(self.mmm, 4, 6, 1)
        self.assertEqual(self.mmm, ['312345','564566','878978','901230'])

    def test_4x6_3t(self):
        self.mmm = ['123456','345678','567890','890123']
        MatrixTurn(self.mmm, 4, 6, 3)
        self.assertEqual(self.mmm, ['853123','987644','097655','123086'])

    def test_6x4_1t(self):
        self.mmm = ['1234','2345','3456','4567','5678','6789']
        MatrixTurn(self.mmm, 6, 4, 1)
        self.assertEqual(self.mmm, ['2123','3434','4545','5656','6767','7898'])

    def test_6x4_3t(self):
        self.mmm = ['1234','2345','3456','4567','5678','6789']
        MatrixTurn(self.mmm, 6, 4, 3)
        self.assertEqual(self.mmm, ['4321','5652','6743','7634','8545','9876'])

    def test_4x6_1t_example(self):
        mmm = ['123456','234567','345678','456789']
        MatrixTurn(mmm, 4, 6, 1)
        self.assertEqual(mmm, ['212345','343456','456767','567898'])


if __name__ == '__main__':
    unittest.main()

