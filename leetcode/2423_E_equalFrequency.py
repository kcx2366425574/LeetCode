#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2423_E_equalFrequency.py
@time: 2023/6/25 22:40
@ide: PyCharm
@desc: 删除字符使频率相同
"""
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:

        values_counter = Counter(list(Counter(word).values()))

        return len(values_counter) == 2 and values_counter[max(values_counter.keys())] == 1
