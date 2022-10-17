#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1267_M_count_servers.py
@time: 2022/10/15 14:54
@ide: PyCharm
@desc: 统计参与通信的服务器
"""


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_sum = [sum(row) for row in grid]
        column_sum = [sum(column) for column in zip(*grid)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row_sum[i] != 1 or column_sum[j] != 1):
                    count += 1
        return count
