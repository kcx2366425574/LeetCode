#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 118_generate.py
@time: 2022/8/2 17:50
@ide: PyCharm
@desc: 杨辉三角
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for i in range(1, numRows):
            tmp_list = [1]
            for index in range(1, len(result[i - 1])):
                tmp_list.append(result[i - 1][index] + result[i - 1][index-1])
            tmp_list.append(1)
            result.append(tmp_list)
        return result
