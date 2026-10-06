# FourBasicOpt.py
# 사칙연산 클래스


class FourBasicOpt:
    """사칙연산(더하기, 빼기, 나누기, 곱하기) 클래스"""

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def divide(self, x, y):
        # test_divide_02 때문에 0으로 나누는 경우는 0 리턴
        if y == 0:
            return 0
        return x / y

    def multiply(self, x, y):
        return x * y
