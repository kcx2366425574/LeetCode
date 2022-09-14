#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 892_surface_area.py
@time: 2022/8/8 14:02
@ide: PyCharm
@desc: 三维形体的表面积
"""


class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        top_bottom = sum([1 for row in grid for value in row if value > 0]) * 2
        left_right = 0
        for row in grid:
            left_right += row[0] + row[-1]
            for i in range(len(row) - 1):
                left_right += abs(row[i] - row[i + 1])

        front_behind = sum([sum(grid[0]), sum(grid[-1])])
        for i in range(len(grid[0]) - 1):
            for j in range(len(grid)):
                front_behind += abs(grid[i][j] - grid[i + 1][j])
        return top_bottom + front_behind + left_right