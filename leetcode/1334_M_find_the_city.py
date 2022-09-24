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


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        ...