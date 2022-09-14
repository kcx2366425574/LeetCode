#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 1337_k_weakest_rows.py
@time: 2022/9/4 23:47
@ide: PyCharm
@desc: 矩阵中战斗力最弱的k行
"""
from collections import defaultdict


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        count = defaultdict(list)

        for index, row in enumerate(mat):
            weight = 0
            for c in row:
                if c == 1:
                    weight += 1
                else:
                    break
            count[weight].append(index)

        ret = []
        for key in sorted(list(count.keys())):
            ret.extend(count[key])
        return ret[:k]
