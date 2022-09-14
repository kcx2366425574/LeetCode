#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 136_single_number.py
@time: 2022/8/25 16:16
@ide: PyCharm
@desc: 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

"""
from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)

        return list(num_set)[0]

    # nb的异或 位运算
    def singleNumber1(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
