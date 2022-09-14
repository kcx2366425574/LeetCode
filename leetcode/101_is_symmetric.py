#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 101_is_symmetric.py
@time: 2022/7/29 18:04
@ide: PyCharm
@desc: 对称二叉树
"""


# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 中序遍历，有问题
    # 无法确定root节点
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        node_list = []

        def middle(r):
            if r is None:
                node_list.append(None)
                return
            if r.left is None and r.right is None:
                node_list.append(r.val)
                return
            else:
                middle(r.left)
                node_list.append(r.val)
                middle(r.right)

        middle(root)
        print(node_list)
        length = len(node_list)

        for i in range(length // 2):
            if node_list[i] != node_list[length - i - 1]:
                return False

        return True

    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:

        def compare(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            compare(left.left, right.right)
            compare(left.right, right.left)
        return compare(root.left, root.right)
