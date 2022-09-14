#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1588_sum_odd_length_subarrays.py
@time: 2022/7/30 11:24
@ide: PyCharm
@desc: 所有奇数长度子数组的和
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

"""


class Solution:

    # 递归递习惯了，不好使
    # 不能去重，也不能不去重
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        num_set = set()

        def compute(sub_array):
            num_set.add(tuple(sub_array))
            if len(sub_array) == 1:
                return
            compute(sub_array[:-2])
            compute(sub_array[1:-1])
            compute(sub_array[2:])

        if len(arr) % 2 == 0:
            compute(arr[:-1])
            compute(arr[1:])
        else:
            compute(arr)

        return sum([sum(d) for d in num_set])

    # 暴力解法。遍历所有的奇数数组
    def sumOddLengthSubarrays1(self, arr: list[int]) -> int:
        sum_count = 0
        for i in range(len(arr)):
            length = 0
            while i + length < len(arr):
                sum_count += sum(arr[i:i+length+1])
                length += 2
        return sum_count


if __name__ == '__main__':
    s = [1, 4, 2, 5, 3, 6, 7]
    print(Solution().sumOddLengthSubarrays1(s))
