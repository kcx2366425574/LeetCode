#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 228_E_summary_ranges.py
@time: 2022/9/21 17:39
@ide: PyCharm
@desc: 汇总区间
"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        nums.append(2 ^ 31 + 2)
        result = []

        start = nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                if start == nums[i]:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i]}")
                start = nums[i + 1]
        return result
