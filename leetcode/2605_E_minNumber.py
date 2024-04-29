#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2605_E_minNumber.py
@time: 2023/9/5 23:32
@ide: PyCharm
@desc: 从两个数字数组里生成最小数字
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        if same := (set(nums1) & set(nums2)):
            return min(same)
        a = min(nums1)
        b = min(nums2)

        return min(b * 10 + a, a * 10 + b)
