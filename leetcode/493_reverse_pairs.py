#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 493_reverse_pairs.py
@time: 2022/8/6 14:24
@ide: PyCharm
@desc: 翻转对
给定一个数组nums，如果i < j且nums[i] > 2*nums[j]我们就将(i, j)称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量

"""


class Solution:
    # 超时。我就说没有这么简单的困难题
    def reversePairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count

    # 分治，归并排序
    def reversePairs1(self, nums: list[int]) -> int:

        nums_len = len(nums)
        n1 = nums[:nums_len // 2]
        n2 = nums[nums_len // 2:]

