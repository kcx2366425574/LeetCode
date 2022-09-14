#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1760_minimum_size.py
@time: 2022/8/11 18:00
@ide: PyCharm
@desc: 袋子里最少数目的球

给你一个整数数组nums，其中nums[i]表示第i个袋子里球的数目。同时给你一个整数maxOperations。

你可以进行如下操作至多maxOperations次：
选择任意一个袋子，并将袋子里的球分到2 个新的袋子中，每个袋子里都有 正整数个球。
比方说，一个袋子里有5个球，你可以把它们分到两个新袋子里，分别有 1个和 4个球，或者分别有 2个和 3个球。
你的开销是单个袋子里球数目的 最大值，你想要 最小化开销。

请你返回进行上述操作后的最小开销。
"""


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        average = sum(nums) // (len(nums) + maxOperations)
        while maxOperations > 0:
            nums.sort()
            nums, last = nums[:-1], nums[-1]
            nums.extend([average, last - average])
            maxOperations -= 1
        return max(nums)
