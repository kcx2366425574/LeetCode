#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2032_E_twoOutOfThree.py
@time: 2022/12/29 22:34
@ide: PyCharm
@desc: 至少在两个数组中出现的值
"""
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list((set(nums1) & set(nums2)) | (set(nums1) & set(nums3)) | (set(nums2) & set(nums3)))
