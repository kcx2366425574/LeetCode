#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 128_M_longest_consecutive.py
@time: 2022/10/22 15:11
@ide: PyCharm
@desc: 最长连续序列
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        current_count = 1
        max_count = 1
        nums.sort()

        if not nums:
            return 0

        for index in range(len(nums) - 1):
            if nums[index + 1] - nums[index] == 1:
                current_count += 1
            elif nums[index + 1] == nums[index]:
                continue
            else:
                max_count = max(max_count, current_count)
                current_count = 1
        return max(max_count, current_count)
