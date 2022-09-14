#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1952_is_three.py
@time: 2022/8/8 15:22
@ide: PyCharm
@desc: 三除数
"""
import math


class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        p = math.pow(n, 0.5)
        if p % 1 != 0:
            return False
        for i in range(2, int(p // 2)):
            if p % i == 0:
                return False
        return True
