#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 104_E_maxDepth.py
@time: 2023/10/29 19:00
@ide: PyCharm
@desc: 二叉树的最大深度
"""
import queue
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def count_depth(node):
            if node is None:
                return 0

            return 1 + max(count_depth(node.left), count_depth(node.right))
        return count_depth(root)

    # 循环
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        node_queue = deque([(1, root)])
        max_depth = 1

        while node_queue:

            depth, cur_node = node_queue.popleft()
            if cur_node.left:
                node_queue.append((depth + 1, cur_node.left))
            if cur_node.right:
                node_queue.append((depth + 1, cur_node.right))
            max_depth = depth

        return max_depth



