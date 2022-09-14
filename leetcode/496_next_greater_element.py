#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 496_next_greater_element.py
@time: 2022/8/22 17:40
@ide: PyCharm
@desc: 下一个更大元素

nums1中数字x的 下一个更大元素 是指x在nums2 中对应位置 右侧 的 第一个 比x大的元素。

给你两个 没有重复元素 的数组nums1 和nums2 ，下标从 0 开始计数，其中nums1是nums2的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素

"""
from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        res = []
        for value in nums1:
            if_find = False
            if_larger = False
            for v2 in nums2:
                if value == v2:
                    if_find = True
                if if_find and v2 > value:
                    res.append(v2)
                    if_larger = True
                    break
            if not if_larger:
                res.append(-1)
        return res

    # 单调栈，下一个更大元素
    def nextGreaterElement1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = deque()
        larger_dict = {}
        for value in nums2[::-1]:
            while stack and stack[-1] <= value:
                stack.pop()

            larger_dict[value] = stack[-1] if stack and stack[-1] > value else -1
            stack.append(value)

        return [larger_dict[v] for v in nums1]
