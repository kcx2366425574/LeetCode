#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1317_get_no_zero_integers.py
@time: 2022/8/6 16:02
@ide: PyCharm
@desc: 将整数转换成两个无零整数和
"""
import random


class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        a, b = 0, 0
        index = 1
        while n > 0:
            tmp = n % 10
            n = n // 10
            if tmp <= 1:
                tmp += 10
                n -= 1
            a = a + index * (tmp // 2)
            b = b + index * (tmp - tmp // 2)
            index *= 10
        return [a, b]

    # 随机大法好
    def getNoZeroIntegers1(self, n: int) -> list[int]:
        while True:
            L = random.randint(1, n)
            R = n - L
            if '0' not in str(L) and '0' not in str(R):
                return [L, R]

    # 枚举……
    def getNoZeroIntegers2(self, n: int) -> list[int]:
        for A in range(1, n):
            B = n - A
            if '0' not in str(A) + str(B):
                return [A, B]
        return []


if __name__ == '__main__':
    num = 1010
    print(Solution().getNoZeroIntegers(num))