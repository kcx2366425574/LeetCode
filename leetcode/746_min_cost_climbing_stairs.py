#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 746_min_cost_climbing_stairs.py
@time: 2022/8/3 10:17
@ide: PyCharm
@desc: 最小花费爬楼梯

给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费
"""


class Solution:
    # 类似菲波那切数列，没有保留中间状态，重复计算
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        def climb(n):
            if n == len(cost) - 1 or n == len(cost) - 2:
                return cost[n]
            return min(cost[n] + climb(n+1), cost[n] + climb(n+2))
        return min(climb(0), climb(1))

    # 动态规划
    def minCostClimbingStairs1(self, cost: list[int]) -> int:
        cost_list = [0 for _ in range(len(cost) + 1)]
        cost_list[0] = 0
        cost_list[1] = 0

        for index in range(2, len(cost)+1):
            cost_list[index] = min(cost_list[index-1] + cost[index-1], cost_list[index-2] + cost[index - 2])
        return cost_list[-1]
