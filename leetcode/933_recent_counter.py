#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 933_recent_counter.py
@time: 2022/7/17 16:40
@ide: PyCharm
@desc: 最近的请求次数
"""
from collections import deque


class RecentCounter:

    def __init__(self):
        # 存储由列表改为队列，耗时更少
        self.count_list = deque()

    def ping(self, t: int) -> int:
        self.count_list.append(t)
        while self.count_list[0] < t - 3000:
            self.count_list.popleft()
        return len(self.count_list)

