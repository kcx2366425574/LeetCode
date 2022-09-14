#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 993_is_cousins.py
@time: 2022/9/8 18:20
@ide: PyCharm
@desc: 二叉树的堂兄弟节点
"""
import copy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        result = []

        def find(node, depth):
            if not node or len(result) == 2:
                return
            if (node.left and node.left.val in (x, y)) or (node.right and node.right.val in (x, y)):
                result.append((node.val, depth))
            find(node.left, depth + 1)
            find(node.right, depth + 1)

        find(root, 0)
        return len(result) == 2 and result[0][0] != result[1][0] and result[0][1] == result[1][1]
