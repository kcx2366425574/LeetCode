#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1663_get_smallest_string.py
@time: 2022/8/8 18:07
@ide: PyCharm
@desc: 具有给定数值的最小字符串
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        while n > 0:
            if k - n + 1 >= 26:
                num = (k - n + 1) // 26
                result.append("z" * num)
                n -= num
                k -= 26 * num
            elif k == n:
                result.append("a" * n)
                n = 0
            else:
                result.append(chr(97 + k - n))
                n -= 1
                k = n
        return "".join(result[::-1])
