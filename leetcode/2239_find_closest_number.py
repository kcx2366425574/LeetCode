#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2239_find_closest_number.py
@time: 2022/8/19 11:51
@ide: PyCharm
@desc: 找到最接近0的数字

给你一个长度为 n 的整数数组 nums ，请你返回 nums 中最 接近 0 的数字。如果有多个答案，请你返回它们中的 最大值 。
"""


class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        res = nums[0]  # 已遍历元素中绝对值最小且数值最大的元素
        dis = abs(nums[0])  # 已遍历元素的最小绝对值
        for num in nums:
            if abs(num) < dis:
                dis = abs(num)
                res = num
            elif abs(num) == dis:
                res = max(res, num)
        return res

