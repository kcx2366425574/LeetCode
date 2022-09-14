#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2022_construct2D_array.py
@time: 2022/7/30 17:59
@ide: PyCharm
@desc: 将一维数组转变为二维数组
"""


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        row = 0
        column = 0
        result_list = [[0 for _ in range(n)] for i in range(m)]
        for value in original:
            result_list[row][column] = value
            column += 1
            if column >= n:
                row += 1
                column = 0
        return result_list

    # 优化。不需要逐个遍历
    def construct2DArray1(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        return [original[i*n:i*n+m] for i in range(m)]

