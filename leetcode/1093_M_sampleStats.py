#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1093_M_sampleStats.py
@time: 2023/5/27 16:02
@ide: PyCharm
@desc: 大样本统计
"""
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        minimum, maximum, median = None, None, None

        # 众数最大个数
        tmp_mode_index = 0
        # 众数值
        mode = None

        # 总数
        total_value = 0
        # 总个数
        total_index = 0

        for i in range(0, 256 // 2):
            head, tail = i, 255 - i
            head_value, tail_value = count[i], count[255 - i]

            if minimum is None and head_value > 0:
                minimum = head
            if maximum is None and tail_value > 0:
                maximum = tail

            if head_value > tmp_mode_index:
                tmp_mode_index = head_value
                mode = head

            if tail_value > tmp_mode_index:
                tmp_mode_index = tail_value
                mode = tail

            total_value += head_value * head + tail_value * tail
            total_index += head_value + tail_value

        return [minimum, maximum, round(total_value / total_index, 5), median, mode]
