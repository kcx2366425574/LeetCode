#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 1403_min_subsequence.py
@time: 2022/8/4 23:32
@ide: PyCharm
@desc: 非递增顺序的最小子序列
"""


class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        for i in range(len(nums) + 1):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]

    # 执行用时：40ms, 在所有Python3提交中击败了99.64 %的用户
    # 内存消耗：14.7MB, 在所有Python3提交中击败了93.45 %的用户
    def minSubsequence1(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        v = 0
        for index, value in enumerate(nums):
            v += value
            if 2 * v > total:
                return nums[:index + 1]
