#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 17.18_shortestSeq.py
@time: 2024/5/1 15:53
@ide: PyCharm
@desc: 最短超串
假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。
"""
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:

        start = 0
        end = 0

        set_small = set(small)

        target_start = None
        target_end = None

        while end < len(big):

            if set_small - set(big[start: end + 1]):
                end += 1
                continue
            else:
                if target_start is None or (target_end - target_start) > (end - start):
                    target_start = start
                    target_end = end
                start += 1

        if target_start is None:
            return []
        else:
            return [target_start, target_end]
