#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 749_contain_virus.py
@time: 2022/7/18 21:35
@ide: PyCharm
@desc: 隔离病毒
"""
import copy
import itertools
from collections import deque


class Solution:

    # 自己写的
    # todo
    def containVirus(self, isInfected: list[list[int]]) -> int:
        len_row = len(isInfected)
        len_column = len(isInfected[0])
        is_settled = copy.deepcopy(isInfected)
        total_firewall = 0

        # 计算当前影响最大的
        def compute_max_effective(status_list, x, y):
            if isInfected[x][y] == 1:
                return compute_max_effective(status_list, x - 1, y) + compute_max_effective(status_list, x + 1, y) + \
                       compute_max_effective(status_list, x, y - 1) + compute_max_effective(status_list, x, y + 1)
            if 0 <= x <= len_row and 0 <= y <= len_column and is_settled[x][y] == 0 and isInfected[x][y] == 0:
                return 1
            return 0

        def set_flag_and_change(status_list, x, y):
            if isInfected[x][y] == 0 and is_settled[x][y] == 0:
                return
            if isInfected[x][y] == 1:
                isInfected[x][y] = -1


        max_count = 0
        max_count_x = 0
        max_count_y = 0
        for x in range(len_row):
            for y in range(len_column):
                if is_settled[x][y] == 1:
                    count = compute_max_effective(is_settled, x, y)
                    if count > max_count:
                        max_count_x = x
                        max_count_y = y

    # 官方题解
    def containVirus1(self, isInfected: list[list[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for d in range(4):
                                nx, ny = x + dirs[d][0], y + dirs[d][1]
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))

                        neighbors.append(neighbor)
                        firewalls.append(firewall)

            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            ans += firewalls[idx]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1

            if len(neighbors) == 1:
                break

        return ans
