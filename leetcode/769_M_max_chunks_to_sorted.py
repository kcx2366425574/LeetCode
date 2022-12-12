#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 769_M_max_chunks_to_sorted.py
@time: 2022/10/13 22:31
@ide: PyCharm
@desc: 最多能完成排序的块
"""


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        count = 0
        current_sum = 0
        for index, num in enumerate(arr):
            if (current_sum := current_sum + num) == index * (index + 1) / 2:
                count += 1
        return count
