# test_FourBasicOpt.py
# 사칙연산 클래스 테스트 (실제 코드보다 먼저 작성)

import unittest
from FourBasicOpt import FourBasicOpt


class FourBasicOptTest(unittest.TestCase):
    def setUp(self):
        self.four_opt = FourBasicOpt()

    # 더하기
    def test_add_01(self):
        self.assertEqual(self.four_opt.add(100, 10), 110)

    def test_add_02(self):
        self.assertEqual(self.four_opt.add(100, -10), 90)

    # 빼기
    def test_subtract_01(self):
        self.assertEqual(self.four_opt.subtract(100, 10), 90)

    def test_subtract_02(self):
        self.assertEqual(self.four_opt.subtract(100, -10), 110)

    # 나누기
    def test_divide_01(self):
        self.assertEqual(self.four_opt.divide(100, 10), 10)

    def test_divide_02(self):
        # 0으로 나누면 에러 대신 0을 돌려주기로 함
        self.assertEqual(self.four_opt.divide(100, 0), 0)

    # 곱하기
    def test_multiply_01(self):
        self.assertEqual(self.four_opt.multiply(100, 10), 1000)

    def test_multiply_02(self):
        self.assertEqual(self.four_opt.multiply(100, 1), 100)

    # 추가로 넣어본 케이스
    def test_add_float(self):
        self.assertAlmostEqual(self.four_opt.add(0.1, 0.2), 0.3)

    def test_divide_negative(self):
        self.assertEqual(self.four_opt.divide(-100, 10), -10)

    def test_multiply_zero(self):
        self.assertEqual(self.four_opt.multiply(100, 0), 0)


if __name__ == '__main__':
    unittest.main()
