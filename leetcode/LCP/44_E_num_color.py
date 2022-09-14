#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 44_E_num_color.py
@time: 2022/9/9 10:20
@ide: PyCharm
@desc: 开幕式焰火颜色种类
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # DFS
    def numColor(self, root: TreeNode) -> int:
        color_set = set()

        def count_color(node):
            if node is None:
                return
            color_set.add(node.val)
            count_color(node.left)
            count_color(node.right)

        count_color(root)
        return len(color_set)

    # BFS
    def numColor1(self, root: TreeNode) -> int:
        node_queue = deque([root])
        color_set = set()
        while node_queue:
            current_node = node_queue.popleft()
            color_set.add(current_node.val)
            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)
        return len(color_set)

