#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 205_E_isIsomorphic.py
@time: 2023/6/24 14:25
@ide: PyCharm
@desc: 同构字符串
"""
from collections import Counter


class Solution:
    # 不行,
    # "bbbaaaba"
    # "aaabbbba"
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        s_num_counter = Counter(list(s_counter.values()))
        t_num_counter = Counter(list(t_counter.values()))

        for s_k, s_v in s_num_counter.items():
            if s_v != t_num_counter[s_k]:
                return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_mapping = {}
        t_mapping = {}

        for single_s, single_t in zip(s, t):
            if single_s not in s_mapping and single_t not in t_mapping:
                s_mapping[single_s] = single_t
                t_mapping[single_t] = single_s
            else:
                if s_mapping.get(single_s) != single_t and t_mapping.get(single_t) != single_s:
                    return False
        return True
