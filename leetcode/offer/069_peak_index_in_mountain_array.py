#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 069_peak_index_in_mountain_array.py
@time: 2022/7/26 10:02
@ide: PyCharm
@desc: 山峰数组的顶部
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        for i in range(1, len(arr) - 1, 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i

    def peakIndexInMountainArray1(self, arr: list[int]) -> int:

        def get_mountain_top(start, end):
            middle = (start + end) // 2
            if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle - 1] < arr[middle] < arr[middle + 1]:
                return get_mountain_top(middle, end)
            else:
                return get_mountain_top(start, middle)
        return get_mountain_top(0, len(arr)-1)
