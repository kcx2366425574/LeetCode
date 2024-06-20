#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2684_M_maxMoves.py
@time: 2024/4/30 14:57
@ide: PyCharm
@desc: 矩阵中移动的最大次数

给你一个下标从 0 开始、大小为 m x n 的矩阵 grid ，矩阵由若干 正 整数组成。

你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid ：

从单元格 (row, col) 可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1)
三个单元格中任一满足值 严格 大于当前单元格的单元格。

返回你在矩阵中能够 移动 的 最大 次数
"""
from collections import deque
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        queue = deque([(i, 0, 0) for i in range(len(grid))])
        max_count = 0
        row = len(grid)
        column = len(grid[0])

        while queue:
            cur_row, cur_col, steps = queue.popleft()

            max_count = max(max_count, steps)
            if max_count == column - 1:
                return max_count

            for offset in [-1, 0, 1]:
                # 行合适
                if 0 < (tmp_row := cur_row + offset) < row:
                    # 列合适
                    if 0 < (tmp_col := cur_col + 1) < column:
                        # 严格大于
                        if grid[tmp_row][tmp_col] > grid[cur_row][cur_col]:
                            queue.append((tmp_row, tmp_col, steps + 1))

        return max_count

    def maxMoves1(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        dq = [[0 for _ in range(column)] for _ in range(row)]

        # 反向遍历列
        for j in range(column - 1):
            # 不包含最后一列
            cur_col = column - j - 2
            # 遍历行
            for i in range(row):

                max_step = 0

                for offset in [-1, 0, 1]:
                    next_column = cur_col + 1
                    next_row = i + offset

                    # 行列位置正确
                    if 0 <= next_row < row and 0 <= next_column < column:
                        # 且左边的数值严格小于右边的
                        if grid[next_row][next_column] > grid[i][cur_col]:
                            max_step = max(max_step, 1 + dq[next_row][next_column])
                dq[i][cur_col] = max_step
        return max([d[0] for d in dq])


if __name__ == '__main__':
    grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
    print(Solution().maxMoves1(grid))
