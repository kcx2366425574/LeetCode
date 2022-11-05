#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 133_M_clone_graph.py
@time: 2022/10/25 16:54
@ide: PyCharm
@desc: 克隆图
"""
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        visit = {}
        queue = deque([node])

        while queue:
            current_node = queue.popleft()
            new_node = Node(current_node.val)
            if new_node.val not in set(visit.keys()):
                visit[new_node.val] = new_node
            for neighbor in current_node.neighbors:
                if neighbor.val not in set(visit.keys()):
                    tmp = Node(neighbor.val)
                    visit[tmp.val] = tmp
                    queue.append(neighbor)
                visit[new_node.val].neighbors.append(visit[neighbor.val])

        return visit[node.val]


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    Solution().cloneGraph(node1)
