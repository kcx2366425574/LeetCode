#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 16.05_trailing_zeroes.py
@time: 2022/8/1 14:21
@ide: PyCharm
@desc: 阶乘尾数
"""


class Solution:
    # 完全想不到
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        while n > 0:
            n = n // 5
            sum += n
        return sum
