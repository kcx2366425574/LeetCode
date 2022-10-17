#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1334_M_find_the_city.py
@time: 2022/9/24 11:17
@ide: PyCharm
@desc: 阈值距离内邻居最少的城市

有 n个城市，按从 0 到 n-1编号。给你一个边数组edges，
其中 edges[i] = [fromi, toi, weighti]代表fromi和toi两个城市之间的双向加权边，距离阈值是一个整数distanceThreshold。

返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为distanceThreshold的城市。如果有多个这样的城市，则返回编号最大的城市。

注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和

"""
from collections import defaultdict, deque


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # init
        city_dict = defaultdict(dict)

        for start, end, distance in edges:
            city_dict[start][end] = distance
            city_dict[end][start] = distance
        min_cities = 500
        ret_result = None
        for city in range(n):
            visit = [[0 for _ in range(n)] for _ in range(n)]
            visit[city][city] = 1
            queue = deque([(city, 0)])
            current_cities = 0
            while queue:
                current_city, current_distance = queue.popleft()
                for next_city, next_distance in city_dict[current_city].items():
                    if current_distance + next_distance <= distanceThreshold and not (
                            visit[city][next_city] and visit[next_city][city]):
                        queue.append((next_city, current_distance + next_distance))
                        visit[city][next_city] = 1
                        visit[next_city][city] = 1
                        current_cities += 1
            if current_cities <= min_cities:
                ret_result = city
                min_cities = current_cities
        return ret_result

    # floyd算法
    def findTheCity1(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        distance = [[float("INF") for _ in range(n)] for _ in range(n)]
        for start, end, dis in edges:
            distance[start][end] = dis
            distance[end][start] = dis

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        ret_result = 100
        min_cities = 500
        for current_city, city_dis in enumerate(distance):
            current_count = 0
            for d in city_dis:
                if d <= distanceThreshold:
                    current_count += 1
            if current_count <= min_cities:
                ret_result = current_city
                min_cities = current_count
        return ret_result


if __name__ == '__main__':
    n = 4
    distanceThreshold = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    Solution().findTheCity1(n, edges, distanceThreshold)
