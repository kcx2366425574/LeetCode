#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1895_largest_magic_square.py
@time: 2022/8/23 16:24
@ide: PyCharm
@desc: 最大的幻方
"""


class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        max_seq = 1
        row = len(grid)
        column = len(grid[0])
        # 以该节点为起始的-|\/方向的四个值
        dp = [[[grid[i][j], grid[i][j], grid[i][j], grid[i][j]] for j in range(column)] for i in range(row)]
        for i in range(2, min(row, column)):
            for r in range(0, row - i + 1):
                for c in range(0, column - i + 1):
                    dp[r][c][0] += grid[r][c + i - 1]
                    dp[r][c][1] += grid[r + i - 1][c]
                    dp[r][c][2] += grid[r + i - 1][c + i - 1]
                    dp[r][c][3] = dp[r][c][3] + grid[r + i - 1][c - i + 1] if c - i + 1 >= 0 else 0

            if_equal = False
            for r in range(0, row - i + 1):
                for c in range(0, column - i + 1):
                    if dp[r][c][0] == dp[r][c][1] == dp[r][c][2] == dp[r][c + i - 1][3]:
                        for tmp in range(1, i):
                            if dp[r][c][0] == dp[r + tmp][c][0] == dp[r][c + tmp][1]:
                                max_seq = i
                                if_equal = True
                                break
                    if if_equal:
                        break
                if if_equal:
                    break
        return max_seq


if __name__ == '__main__':
    grid = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
    print(Solution().largestMagicSquare(grid))
