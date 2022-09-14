#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 16.11_diving_board.py
@time: 2022/9/3 11:18
@ide: PyCharm
@desc: 
"""


class Solution:
    # 递归会超时
    def divingBoard(self, shorter: int, longer: int, k: int) -> list[int]:
        ret = []

        def diving(left_k, sum):
            if left_k == 0:
                if sum != 0:
                    ret.append(sum)
                return

            diving(left_k - 1, sum + shorter)
            diving(left_k - 1, sum + longer)

        diving(k, 0)
        return ret

    # 还是超时
    def divingBoard1(self, shorter: int, longer: int, k: int) -> list[int]:
        if k == 0:
            return []
        ret = [0]
        while k > 0:
            short = list(map(lambda x: x + shorter, ret))
            long = list(map(lambda x: x + longer, ret))
            ret = short + long
            k -= 1
        return ret

    def divingBoard2(self, shorter: int, longer: int, k: int) -> list[int]:
        if k == 0:
            return []
        return [long_count * longer + (k - long_count) * shorter for long_count in range(k + 1)]
