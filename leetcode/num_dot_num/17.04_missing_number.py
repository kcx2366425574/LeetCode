#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 17.04_missing_number.py
@time: 2022/7/16 17:20
@ide: PyCharm
@desc: 消失的数字
数组nums包含从0到n的所有整数，但其中缺了一个。
在O(n)时间内找出那个缺失的整数。
"""


class Solution:
    # 暴力循环
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    # 将list转为set, 耗时减少，但内存增加
    def missingNumber1(self, nums: list[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i

    # 自己写的, 本来想递归的，结果不好使
    # 没用
    def missingNumber2(self, nums: list[int]) -> int:
        num_sorted = sorted(nums)

        def find_missing(start, end):
            middle = (start + end) // 2
            if middle >= num_sorted[middle]:
                return middle if end - middle == 1 else find_missing(middle, end)
            elif middle < num_sorted[middle]:
                return middle if middle - start == 1 else find_missing(start, middle)

        return find_missing(0, len(nums))

    # 用数学方法……
    def missingNumber3(self, nums: list[int]) -> int:
        n = len(nums)
        return n*(n + 1)//2 - sum(nums)


if __name__ == '__main__':

    nums = [0, 3, 2]
    s = Solution()
    print(s.missingNumber2(nums))
