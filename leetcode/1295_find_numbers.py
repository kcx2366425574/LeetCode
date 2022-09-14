#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1295_find_numbers.py
@time: 2022/9/8 14:12
@ide: PyCharm
@desc: 统计位数为偶数的数字
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum([1 for num in nums if len(str(num)) % 2 == 0])
