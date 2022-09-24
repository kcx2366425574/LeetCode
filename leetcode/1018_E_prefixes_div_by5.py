#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1018_E_prefixes_div_by5.py
@time: 2022/9/24 10:01
@ide: PyCharm
@desc: 
"""


class Solution:
    # 将二进制转十进制
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        current = ""
        result = [False for i in range(len(nums))]
        for index, num in enumerate(nums):
            current += str(num)
            if int(current, 2) % 5 == 0:
                result[index] = True
        return result

    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = []
        current = 0
        for num in nums:
            current = ((current << 1) + num) % 5
            result.append(current == 0)
        return result
