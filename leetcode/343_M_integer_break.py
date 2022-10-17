#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 343_M_integer_break.py
@time: 2022/10/14 11:53
@ide: PyCharm
@desc: 整数拆分
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
