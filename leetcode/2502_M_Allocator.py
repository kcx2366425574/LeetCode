#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2502_M_Allocator.py
@time: 2022/12/17 19:32
@ide: PyCharm
@desc: 设计内存分配器
"""
from collections import defaultdict


class Allocator:

    def __init__(self, n: int):
        self.data = [-1 for _ in range(n)]
        self.detail = defaultdict(set)

    def allocate(self, size: int, mID: int) -> int:
        free_count = []
        ret_index = -1
        for index, num in enumerate(self.data):
            if num == -1:
                free_count.append(index)
                if len(free_count) == size:
                    ret_index = free_count[0]
                    for i in free_count:
                        self.detail[mID].add(i)
                        self.data[i] = mID
                    break
            else:
                free_count = []
        return ret_index

    def free(self, mID: int) -> int:
        count = len(self.detail[mID])
        for index in self.detail[mID]:
            self.data[index] = -1
        self.detail[mID] = set()
        return count


class Allocator:

    def __init__(self, n: int):
        self.size = n
        # 已经使用的内存单元
        self.used_index = set()
        # 每个mID分别赋给了哪些内存单元
        self.detail = defaultdict(set)

    def allocate(self, size: int, mID: int) -> int:
        index_count = []
        ret_count = -1
        for i in range(self.size):
            # 如果内存单元还未被分配
            if i not in self.used_index:
                index_count.append(i)
                if len(index_count) == size:
                    # 如果刚好满足大小要求
                    ret_count = index_count[0]
                    self.used_index.update(index_count)
                    self.detail[mID].update(index_count)
                    break
            else:
                index_count = []
        return ret_count

    def free(self, mID: int) -> int:
        count = len(self.detail[mID])
        for index in self.detail[mID]:
            self.used_index.remove(index)
        self.detail[mID] = set()
        return count
