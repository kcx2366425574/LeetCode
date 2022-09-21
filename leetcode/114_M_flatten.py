#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 114_M_flatten.py
@time: 2022/9/20 18:53
@ide: PyCharm
@desc: 二叉树展开为链表
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 非原地修改，先序遍历所有的节点，再构造链表
    def flatten1(self, root: Optional[TreeNode]) -> TreeNode:
        pre_list = []

        def pre_order(node):
            if not node:
                return
            pre_list.append(node)
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        for i in range(len(pre_list) - 1):
            parent, right_node = pre_list[i], pre_list[i + 1]
            parent.left = None
            right_node.left = None
            parent.right = right_node

    # 原地修改
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr
