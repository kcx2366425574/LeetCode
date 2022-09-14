#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 119_get_row.py
@time: 2022/8/2 17:21
@ide: PyCharm
@desc: 杨辉三角
"""


class Solution:
    # 原地滚动更新
    def getRow(self, rowIndex: int) -> list[int]:
        arr = [0 for i in range(rowIndex + 1)]
        arr[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                arr[j] = arr[j] + arr[j - 1]
        return arr

