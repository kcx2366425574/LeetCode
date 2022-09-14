#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 168_convert_to_title.py
@time: 2022/8/5 11:34
@ide: PyCharm
@desc: Excel表列名称

给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + 65))
            columnNumber //= 26

        return "".join(result[::-1])
