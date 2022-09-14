#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 883_projection_area.py
@time: 2022/8/1 11:43
@ide: PyCharm
@desc: 三维形体投影面积

只要弄清楚面积是怎么算的就简单了，
需要找出每行的最大值，侧视图投影面积
找出每列的最大值，主视图投影面积
找出所有非0元素的个数，俯视图的投影面积
"""


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        sum_row = 0
        max_column = [0 for _ in range(n)]
        for i in range(n):
            sum_row += max(grid[i])
            for j in range(n):
                max_column[i] = max(max_column[i], grid[j][i])
        no_zero = len([v for v_list in grid for v in v_list if v != 0])
        return sum_row + sum(max_column) + no_zero
