#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1329_M_diagonalSort.py
@time: 2024/4/29 17:11
@ide: PyCharm
@desc: 将矩阵按对角线排序


矩阵对角线 是一条从矩阵最上面行或者最左侧列中的某个元素开始的对角线，沿右下方向一直到矩阵末尾的元素。
例如，矩阵 mat 有 6 行 3 列，从 mat[2][0] 开始的 矩阵对角线 将会经过 mat[2][0]、mat[3][1] 和 mat[4][2] 。

给你一个 m * n 的整数矩阵 mat ，请你将同一条 矩阵对角线 上的元素按升序排序后，返回排好序的矩阵。
"""
import copy
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        row = len(mat)
        column = len(mat[0])
        ret_array = copy.deepcopy(mat)

        for i in range(row):

            # 排序
            r, c = i, 0
            tmp_list = []
            while r < row and c < column:
                tmp_list = self.bisect(tmp_list, mat[r][c])
                r += 1
                c += 1

            # 赋值
            r, c = i, 0
            while r < row and c < column:
                ret_array[r][c] = tmp_list[c]
                r += 1
                c += 1

        for i in range(1, column):

            # 排序
            r, c = 0, i
            tmp_list = []
            while r < row and c < column:
                tmp_list = self.bisect(tmp_list, mat[r][c])
                r += 1
                c += 1

            # 赋值
            r, c = 0, i
            while r < row and c < column:
                ret_array[r][c] = tmp_list[r]
                r += 1
                c += 1
        return ret_array

    def bisect(self, array: List[int], value: int):
        """
        将指定值插入到有序列表中
        :param array: 已知数组
        :param value: 待插入的值
        :return: 插入后的有序数组
        """
        # 空数组
        if not array:
            return [value]
        # 比最小值小或者比最大值大
        if array[0] > value:
            return [value] + array
        if array[-1] <= value:
            return array + [value]

        middle = len(array) // 2
        middle_value = array[middle]

        if middle_value >= value:
            return self.bisect(array[:middle], value) + array[middle:]
        else:
            return array[:middle] + self.bisect(array[middle:], value)
