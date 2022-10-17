#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1753_M_maximum_score.py
@time: 2022/10/15 15:25
@ide: PyCharm
@desc: 移除石子的最大得分
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stone_list = [a, b, c]
        stone_list.sort()
        result = 0
        while stone_list[1] != 0:
            stone_list[1] = stone_list[1] - 1
            stone_list[2] = stone_list[2] - 1
            stone_list.sort()
            result += 1
        return result
