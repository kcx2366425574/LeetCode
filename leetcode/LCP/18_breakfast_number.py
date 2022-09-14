#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 18_breakfast_number.py
@time: 2022/8/19 13:54
@ide: PyCharm
@desc: 早餐组合

小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

"""


class Solution:

    # 超出时间限制
    def breakfastNumber(self, staple: list[int], drinks: list[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        count = 0

        for s in staple:
            for d in drinks:
                if s + d > x:
                    break
                count += 1
        return count % 1000000007

    # 最大递归深度报错
    def breakfastNumber1(self, staple: list[int], drinks: list[int], x: int) -> int:

        def find_index(target_value, start, end):
            if end - start == 1:
                if drinks[end] + target_value <= x:
                    return end
                elif drinks[start] + target_value <= x:
                    return start
                else:
                    return -1
            middle = (start + end) // 2
            if target_value + drinks[middle] <= x:
                return find_index(target_value, middle, end)
            else:
                return find_index(target_value, start, middle)

        drinks.sort()
        count = 0

        for s in staple:
            count += (find_index(s, 0, len(drinks)-1) + 1)
        return count % 1000000007

    def breakfastNumber2(self, staple: list[int], drinks: list[int], x: int) -> int:

        drinks.sort()

        for s in staple:
            count = 0
            start = 0
            end = len(drinks) - 1
            while end - start != 1:
                if drinks[start] + s > x:
                    break
                if drinks[end] + s <= x:
                    count += (end + 1)
                    break
                middle = (start + end) // 2
                if drinks[middle] + s <= x:
                    start, end = middle, end
                else:
                    start, end = start, middle


if __name__ == '__main__':
    staple = [10, 20, 5]
    drinks = [5, 5, 2]
    x = 15
    print(Solution().breakfastNumber1(staple, drinks, x))
