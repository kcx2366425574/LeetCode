#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 209_M_minSubArrayLen.py
@time: 2023/8/2 13:12
@ide: PyCharm
@desc: 长度最小的子数组
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        total = 0
        min_len = len(nums) + 1

        while right <= len(nums) - 1:

            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != len(nums) + 1 else 0
