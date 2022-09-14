#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1437_k_length_apart.py
@time: 2022/7/30 17:45
@ide: PyCharm
@desc: 是否所有1都至少相隔k各元素
"""


class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_location = None
        for index in range(len(nums)):
            if nums[index] == 1:
                if last_location is not None and index - last_location != k + 1:
                    return False
                last_location = index
        return True
