#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 442_find_duplicates.py
@time: 2022/8/11 0:02
@ide: PyCharm
@desc: 数组中重复的数据

给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums.sort()
        result = []

        current = 0
        for num in nums:
            if num == current:
                result.append(num)
            current = num

        return result
