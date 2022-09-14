#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1672_maximum_wealth.py
@time: 2022/7/30 17:38
@ide: PyCharm
@desc: 最富有客户的资产总量
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for l in accounts:
            max_wealth = max(max_wealth, sum(l))
        return max_wealth

    # pythonic 一行搞定
    def maximumWealth1(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))
