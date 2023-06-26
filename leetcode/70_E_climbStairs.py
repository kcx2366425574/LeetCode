#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 70_E_climbStairs.py
@time: 2023/6/19 21:13
@ide: PyCharm
@desc: 爬楼梯
"""
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b

