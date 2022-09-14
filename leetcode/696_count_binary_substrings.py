#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 696_count_binary_substrings.py
@time: 2022/8/31 18:00
@ide: PyCharm
@desc: 计数二进制子串

给定一个字符串s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。

"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        sum_count = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                interval = 0
                while i - interval >= 0 and i + 1 + interval <= len(s) - 1 and s[i - interval] == s[i] and s[i + 1] == s[i + 1 + interval]:
                    sum_count += 1
                    interval += 1
        return sum_count

    # 官方题解，按字符分组
    def countBinarySubstrings1(self, s: str) -> int:
        count_list = []
        last_value = s[0]
        last_count = 1
        for i in range(1, len(s)):
            if last_value != s[i]:
                count_list.append(last_count)
                last_value = s[i]
                last_count = 1
            else:
                last_count += 1
        count_list.append(last_count)

        return sum(min(count_list[i], count_list[i + 1]) for i in range(0, len(count_list) - 1))
