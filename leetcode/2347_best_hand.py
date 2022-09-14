#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2347_best_hand.py
@time: 2022/9/1 11:25
@ide: PyCharm
@desc: 最好的扑克手牌
"""
from collections import Counter


class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        max_count = Counter(ranks).most_common(1)[0][1]
        if max_count >= 3:
            return "Three of a Kind"
        elif max_count == 2:
            return "Pair"
        else:
            return "High Card"
