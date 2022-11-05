#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1704_E_halves_are_alike.py
@time: 2022/10/21 15:12
@ide: PyCharm
@desc: 判断字符串的两半是否相似
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0

        for i, char in enumerate(s):
            if char.upper() in "AEIOU":
                if i < len(s) // 2:
                    count += 1
                else:
                    count -= 1
        return count == 0
