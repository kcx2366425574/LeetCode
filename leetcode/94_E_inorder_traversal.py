#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 94_E_inorder_traversal.py
@time: 2022/10/15 15:56
@ide: PyCharm
@desc: 二叉树的中序遍历
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            result.append(node.val)
            in_order(node.right)

        in_order(root)
        return result

    # 高级迭代
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        stack = [root]
        result = []

        while stack:
            cur = stack.pop()
            if isinstance(cur, int):
                result.append(cur)
            elif isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.val, cur.left])
        return result
