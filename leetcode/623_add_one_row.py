#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 623_add_one_row.py
@time: 2022/8/5 0:57
@ide: PyCharm
@desc: 在二叉树中增加一行
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val=val)
            node.left = root
            return node

        def find_depth(r, d):
            if r is None:
                return
            if d == depth:
                node = TreeNode(val=val)
                node.left = r.left
                r.left = node

                node_right = TreeNode(val=val)
                node_right.right = r.right
                r.right = node_right

            if r.left:
                find_depth(r.left, d + 1)
            if r.right:
                find_depth(r.right, d + 1)

        find_depth(root, 2)
        return root
