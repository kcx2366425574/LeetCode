#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 55_M_canJump.py
@time: 2023/9/5 23:42
@ide: PyCharm
@desc: 跳跃游戏
"""
from collections import deque
from typing import List


class Solution:

    # 广度优先，太慢了
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        visited = [0 for _ in range(len(nums))]
        current_state = deque([0])
        visited[0] = 1

        last = len(nums) - 1

        while current_state:
            # 当前索引位置
            cur = current_state.popleft()
            # 当前能跳跃的最大数
            value = nums[cur]

            for i in range(1, value + 1):
                next_state = cur + i
                if next_state != last:
                    if visited[next_state] == 0:
                        current_state.append(next_state)
                        visited[next_state] = 1
                else:
                    return True
        return False
