#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 1475_final_prices.py
@time: 2022/9/1 0:19
@ide: PyCharm
@desc: 商品折扣的最终价格
"""
from collections import deque


class Solution:
    # 单调栈
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = [0 for _ in prices]
        stack = deque()
        for index, value in enumerate(prices[::-1], 1):
            while stack and stack[-1] > value:
                stack.pop()
            res[-index] = prices[-index] - stack[-1] if stack else prices[-index]
            stack.append(value)
        return res
