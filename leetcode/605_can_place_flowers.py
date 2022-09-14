#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 605_can_place_flowers.py
@time: 2022/8/8 18:43
@ide: PyCharm
@desc: 种花问题
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        if n == 0:
            return True

        flowerbed = [0, *flowerbed, 0]

        i = 1
        while i <= len(flowerbed) - 2:
            if flowerbed[i] == 1:
                i += 2
                continue
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                i += 2
                if n == 0:
                    return True
            else:
                i += 1
        return False
