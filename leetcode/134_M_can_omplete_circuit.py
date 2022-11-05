#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@file: 134_M_can_omplete_circuit.py
@time: 2022/11/4 16:31
@ide: PyCharm
@desc: 加油站
"""
import copy
from typing import List


class Solution:

    # 超出时间限制
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if_can_start = {}
        for index, g in enumerate(gas):
            if (new_detail := g - cost[index]) >= 0:
                if_can_start[index] = new_detail

        for i in range(1, n):
            print(len(if_can_start))
            temp_dict = copy.deepcopy(if_can_start)
            for index, detail in temp_dict.items():
                new_index = (index + i) % n
                if (new_detail := detail + gas[new_index] - cost[new_index]) >= 0:
                    if_can_start[index] = new_detail
                else:
                    if_can_start.pop(index)
        return list(if_can_start.values())[0]

    # 虽然过了，但是效率太低了
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_end_with_rest = {}
        n = len(gas)
        for i in range(n-1, -1, -1):
            current_rest = 0
            end = i
            while (tmp_rest := current_rest + gas[end] - cost[end]) >= 0:
                end = (end + 1) % n
                current_rest = tmp_rest
                if end in start_end_with_rest:
                    current_rest = current_rest + start_end_with_rest[end]["rest"]
                    end = start_end_with_rest[end]["end"]
                else:
                    current_rest = tmp_rest
                if end == i:
                    return end
            start_end_with_rest[i] = {"end": end, "rest": current_rest}

        return -1


if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas, cost))