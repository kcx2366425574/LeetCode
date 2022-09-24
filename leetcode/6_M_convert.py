#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 6_M_convert.py
@time: 2022/9/24 10:44
@ide: PyCharm
@desc: z字形变换
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        data = [[] for i in range(numRows)]
        current_row = 0
        flag = 1

        for ch in s:
            data[current_row].append(ch)
            if current_row == numRows - 1:
                flag = -1
            elif current_row == 0:
                flag = 1
            current_row += flag

        return "".join(["".join(i) for i in data])
