#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2373_largest_local.py
@time: 2022/9/3 14:10
@ide: PyCharm
@desc: 矩阵中的局部最大值
"""


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        length = len(grid) - 1
        result = [[0 for _ in range(length - 1)] for _ in range(length - 1)]
        index = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(1, length):
            for column in range(1, length):
                result[row - 1][column - 1] = max(
                    [grid[row + r_index][column + c_index] for r_index, c_index in index])
        return result

