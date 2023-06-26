#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1262_M_maxSumDivThree.py
@time: 2023/6/19 20:16
@ide: PyCharm
@desc: 可被三整除的最大和
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        total_sum = 0
        rest_num = []
        for n in nums:
            if n % 3 == 0:
                total_sum += n
            else:
                rest_num.append(n)

        if not rest_num:
            return total_sum

        rest_num.sort(reverse=True)

        num_dict = defaultdict(deque)
        for sort_n in rest_num:
            sort_sub = sort_n % 3
            if num_dict[3 - sort_sub]:
                cur = num_dict[3 - sort_sub].popleft()
                total_sum += (sort_n + cur)
            else:
                num_dict[sort_sub].append(sort_n)
        return total_sum

    def maxSumDivThree(self, nums: List[int]) -> int:

        nums.sort()
        nums1 = []
        nums2 = []
        for n in nums:
            div = n % 3
            if div == 1:
                nums1.append(n)
            elif div == 2:
                nums2.append(n)

        total_sum = sum(nums)

        total_div = total_sum % 3

        if total_div == 1:
            tmp = []
            if nums1:
                tmp.append(nums1[0])
            if len(nums2) >= 2:
                tmp.append(nums2[0] + nums2[1])
            return total_sum - min(tmp) if total_sum else 0
        elif total_div == 2:
            tmp = []
            if nums2:
                tmp.append(nums2[0])
            if len(nums1) >= 2:
                tmp.append(nums1[0] + nums1[1])
            return total_sum - min(tmp) if total_sum else 0
        return total_sum
