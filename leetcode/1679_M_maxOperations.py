#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1679_M_maxOperations.py
@time: 2022/12/29 22:53
@ide: PyCharm
@desc: K 和数对的最大数目
"""
import copy
from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        tmp = copy.deepcopy(d)
        count = 0

        for key, value in tmp.items():
            if d.get(key, 0) > 0 and d.get(k - key, 0) > 0:
                count += 1
                d[key] = d[key] - 1
                d[k-key] = d[k-key] - 1
        return count
