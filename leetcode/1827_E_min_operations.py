#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1827_E_min_operations.py
@time: 2022/10/15 14:39
@ide: PyCharm
@desc: 最少操作使数组递增
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        max_num = nums[0]
        incr_count = 0
        for num in nums[1:]:
            if num <= max_num:
                incr_count += max_num - num + 1
                max_num += 1
            else:
                max_num = num
        return incr_count
