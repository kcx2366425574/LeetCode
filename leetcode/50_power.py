#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 50_power.py
@time: 2022/7/13 19:34
@ide: PyCharm
@desc: 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ).
"""


class Solution:
    # 自己写的，什么狗屎，
    # decimal溢出
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or n == 0:
            return 1.0
        from decimal import Decimal
        ret_sum = Decimal("1.0")
        array_temp = [{0: 1}, {1: Decimal(f"{x}")}]
        start = 1
        abs_n = abs(n)
        while start < abs_n:
            value = array_temp[-1].get(start) * array_temp[-1].get(start)
            start *= 2
            array_temp.append({start: value})

        for single_data in array_temp[::-1]:
            power = list(single_data.keys())[0]
            if power > abs_n:
                continue
            else:
                ret_sum *= single_data[power]
                abs_n -= power
            if abs_n == 0:
                break
        return float(ret_sum) if n > 0 else float(Decimal("1.0") / ret_sum)

    # 递归
    def pow(self, x: float, n: int) -> float:

        def quick_pow(count):
            if count == 0:
                return 1.0
            else:
                y = quick_pow(count // 2)
                return y * y if count % 2 == 0 else y * y * x

        return quick_pow(n) if n >= 0 else 1 / quick_pow(-n)

    # 迭代
    def pow1(self, x: float, n: int) -> float:
        if n == 0 or x == 0:
            return 1.0

        def quick_pow(count):
            result = 1
            tmp = x
            while count > 0:
                if count % 2 == 1:
                    result *= tmp
                tmp = tmp * tmp
                count = count // 2
            return result

        return quick_pow(n) if n >= 0 else 1.0 / quick_pow(-n)


if __name__ == '__main__':

    x = 2.0
    n = 10
    s = Solution()
    print(s.pow1(x, n))
    print(s.pow(x, n))
