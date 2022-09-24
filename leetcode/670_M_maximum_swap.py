#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 670_M_maximum_swap.py
@time: 2022/9/21 18:49
@ide: PyCharm
@desc: 
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = list(str(num))
        num_len = len(str_num)
        if_first = True
        min_swap = None
        max_swap = None
        for i in range(num_len - 1):
            for j in range(i + 1, num_len):
                if int(str_num[j]) > int(str_num[i]):
                    if_first = False
                    min_swap = i
                    if max_swap is None or int(str_num[max_swap]) <= int(str_num[j]):
                        max_swap = j
            if not if_first:
                break

        if min_swap is not None and max_swap is not None:
            str_num[min_swap], str_num[max_swap] = str_num[max_swap], str_num[min_swap]
            return int("".join(str_num))
        else:
            return num

    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))
