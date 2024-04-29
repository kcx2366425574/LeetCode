#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 058_E_reverseLeftWords.py
@time: 2023/8/1 22:55
@ide: PyCharm
@desc: 左旋转字符串
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:

        index = n % len(s)
        return s[index:] + s[:index]
