#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 695_M_maxAreaOfIsland.py
@time: 2024/6/20 11:37
@ide: PyCharm
@desc: 岛屿的最大面积

给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
"""
from typing import List


class Solution:

    def get_count(self, row, column, data):
        if not (0 <= row < len(data) and 0 <= column < len(data[0]) and data[row][column] == 1):
            return 0

        data[row][column] = 0
        return 1 + self.get_count(row - 1, column, data) + self.get_count(row + 1, column, data) + self.get_count(
            row, column + 1, data) + self.get_count(row, column - 1, data)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        row = len(grid)
        column = len(grid[0])

        for i in range(row):

            for j in range(column):

                max_area = max(max_area, self.get_count(i, j, grid))
        return max_area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    result = Solution().maxAreaOfIsland(grid)
    print(result)
