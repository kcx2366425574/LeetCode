#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1502_max_satisfied.py
@time: 2022/8/5 9:52
@ide: PyCharm
@desc: 爱生气的书店老板
有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。

当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。

请你返回 这一天营业下来，最多有多少客户能够感到满意 。

"""


class Solution:

    # 执行用时：56 ms, 在所有 Python3 提交中击败了98.48%的用
    # 内存消耗：16.8 MB, 在所有 Python3 提交中击败了71.99%的用户
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        max_satisfie = 0
        max_index = 0
        ret_cus = 0
        tmp_sum = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                ret_cus += customers[i]
            if i < minutes:
                tmp_sum += customers[i] * grumpy[i]
            else:
                tmp_sum = tmp_sum - customers[i - minutes] * grumpy[i - minutes] + customers[i] * grumpy[i]
            if tmp_sum > max_satisfie:
                max_satisfie = tmp_sum
                max_index = i - minutes + 1 if i - minutes + 1 >= 0 else 0

        end = min(max_index + minutes, len(customers))
        for index in range(max_index, end):
            if grumpy[index] == 1:
                ret_cus += customers[index]
        return ret_cus


if __name__ == "__main__":
    customers = [4, 10, 10]
    grumpy = [1, 1, 0]
    minutes = 2
    print(Solution().maxSatisfied(customers, grumpy, minutes))

