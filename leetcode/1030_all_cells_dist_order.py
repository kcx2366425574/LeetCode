#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1030_all_cells_dist_order.py
@time: 2022/7/25 16:26
@ide: PyCharm
@desc: 距离顺序排序矩阵单元格

给定四个整数 row, cols , rCenter 和 cCenter 。有一个rows x cols的矩阵，你在单元格上的坐标是(rCenter, cCenter) 。

返回矩阵中的所有单元格的坐标，并按与(rCenter, cCenter)的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。

单元格(r1, c1) 和 (r2, c2) 之间的距离为|r1 - r2| + |c1 - c2|。

"""
from collections import deque, defaultdict


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        flag = [[0 for i in range(cols)] for j in range(rows)]

        point_dq = deque([[rCenter, cCenter]])
        flag[rCenter][cCenter] = 1
        result = []
        while len(result) < rows * cols:
            center = point_dq.popleft()
            result.append(center)
            for d in directions:
                x, y = center[0] + d[0], center[1] + d[1]
                if 0 <= x <= rows - 1 and 0 <= y <= cols - 1 and flag[x][y] == 0:
                    point_dq.append([x, y])
                    flag[x][y] = 1
        return result

    # 效率更高
    def allCellsDistOrder1(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:

        data = defaultdict(list)
        result = []
        for i in range(rows):
            for j in range(cols):
                data[abs(rCenter - i) + abs(cCenter - j)].append((i, j))
        for i in range(cols + rows):
            if not data[i]:
                break
            result.extend(data[i])
        return result
