#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 1260_shift_grid.py
@time: 2022/7/21 1:16
@ide: PyCharm
@desc: 二维网格的迁移
"""
import copy


class Solution:

    # 自己写的,过了
    # 执行用时：68 ms, 在所有 Python3 提交中击败了44.10% 的用户
    # 内存消耗：15.4 MB, 在所有 Python3 提交中击败了35.37%的用户
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        x = len(grid)
        y = len(grid[0])
        temp_k = k % (x * y)
        end_x = temp_k // y
        temp_k = temp_k % y

        ret_list = copy.deepcopy(grid)
        for i in range(x):
            for j in range(y):
                ret_list[end_x][temp_k] = grid[i][j]
                temp_k += 1
                if temp_k == y:
                    end_x += 1
                    temp_k = 0
                if end_x == x:
                    end_x = 0
        return ret_list


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    s = Solution()
    print(s.shiftGrid(grid, k))
