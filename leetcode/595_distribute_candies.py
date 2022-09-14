#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 595_distribute_candies.py
@time: 2022/8/19 10:16
@ide: PyCharm
@desc: 分糖果
"""


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
