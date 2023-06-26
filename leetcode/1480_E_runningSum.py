#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1480_E_runningSum.py
@time: 2023/6/25 22:33
@ide: PyCharm
@desc:  一维数组的动态和
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        res = [0 for _ in range(len(nums) + 1)]

        for index, num in enumerate(nums):
            res[index + 1] = res[index] + num

        return res[1:]
