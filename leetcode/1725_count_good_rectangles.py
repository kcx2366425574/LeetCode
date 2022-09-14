#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1725_count_good_rectangles.py
@time: 2022/9/5 18:04
@ide: PyCharm
@desc: 可以形成最大正方形的矩阵数目
"""


class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        max_value = -1
        value_count = 0

        for tup in rectangles:
            m = min(tup)
            if m == max_value:
                value_count += 1
            elif m > max_value:
                max_value = m
                value_count = 1
        return value_count
