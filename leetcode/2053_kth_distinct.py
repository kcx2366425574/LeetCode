#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2053_kth_distinct.py
@time: 2022/7/26 10:55
@ide: PyCharm
@desc: 第k个独一无二的字符串
"""
from collections import defaultdict, Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:

        nums_count = defaultdict(int)
        for index in arr:
            nums_count[index] += 1

        flag = 0
        for a in arr:
            if nums_count[a] == 1:
                flag += 1
                if flag == k:
                    return a
        return ""

    def kthDistinct1(self, arr: list[str], k: int) -> str:

        nums_count = Counter(arr)

        for a in arr:
            if nums_count[a] == 1:
                k -= 1
                if k == 0:
                    return a
        return ""
