#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 54_M_spiral_order.py
@time: 2022/9/17 11:38
@ide: PyCharm
@desc: 螺旋矩阵
"""
from collections import deque


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        order_list = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        ret_list = [matrix[0][0]]
        matrix[0][0] = -520
        row = len(matrix)
        column = len(matrix[0])
        total_len = row * column

        current_direction = order_list.popleft()
        start_pos = (0, 0)
        while len(ret_list) < total_len:
            next_x = start_pos[0] + current_direction[0]
            next_y = start_pos[1] + current_direction[1]
            if 0 <= next_x < row and 0 <= next_y < column and matrix[next_x][next_y] != -520:
                ret_list.append(matrix[next_x][next_y])
                matrix[next_x][next_y] = -520
                start_pos = (next_x, next_y)
            else:
                next_x -= current_direction[0]
                next_y -= current_direction[1]
                order_list.append(current_direction)
                current_direction = order_list.popleft()
        return ret_list

    # nb
    def spiralOrder1(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res.extend(matrix.pop(0))
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]
        return res
