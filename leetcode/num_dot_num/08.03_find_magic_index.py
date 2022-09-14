#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 08.03_find_magic_index.py
@time: 2022/8/25 20:49
@ide: PyCharm
@desc: 找到魔术索引，索引=实际值
"""


class Solution:
    def findMagicIndex(self, nums: list[int]) -> int:
        for index, value in enumerate(nums):
            if index == value:
                return index
        return -1
