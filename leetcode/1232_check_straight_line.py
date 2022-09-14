#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 1232_check_straight_line.py
@time: 2022/7/21 22:59
@ide: PyCharm
@desc: 判断点是否都在同一直线上
"""


class Solution:

    # 注意使用乘法
    # 除法由于精度问题，并且性能较低
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        for index in range(1, len(coordinates) - 1):
            if ((coordinates[index][1] - coordinates[index - 1][1]) * (
                    coordinates[index + 1][0] - coordinates[index][0])) != \
                    ((coordinates[index + 1][1] - coordinates[index][1]) * (
                            coordinates[index][0] - coordinates[index - 1][0])):
                return False
        return True
