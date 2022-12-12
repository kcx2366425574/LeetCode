#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2248_E_intersection.py
@time: 2022/12/13 1:01
@ide: PyCharm
@desc: 多个数组求交集
"""
import functools
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        return sorted(functools.reduce(lambda a, b: set(a) & (set(b)), nums))
