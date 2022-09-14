#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 401_read_binary_watch.py
@time: 2022/8/19 10:31
@ide: PyCharm
@desc: 二进制手表
"""
from itertools import combinations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        time_list = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        res = []
        for comb in combinations(range(10), turnedOn):
            hour = sum(time_list[i] for i in comb if i <= 3)
            minutes = sum(time_list[i] for i in comb if i >= 4)
            if 0 <= hour <= 11 and 0 <= minutes <= 59:
                minutes = str(minutes) if len(str(minutes)) == 2 else f"0{str(minutes)}"
                res.append(f"{hour}:{minutes}")
        return res
