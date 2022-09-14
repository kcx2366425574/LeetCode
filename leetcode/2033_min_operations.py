#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2033_min_operations.py
@time: 2022/8/5 18:42
@ide: PyCharm
@desc: 获取单值网络的最小操作数
"""


class Solution:
    # 排序后取中位数计算即可
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        ret, li = 0, []
        for i in grid:
            li.extend(i)
        li.sort()
        mid = li[len(li) // 2]
        for v in li:
            if abs(mid - v) % x:
                return -1
            ret += abs(mid - v) // x
        return ret
