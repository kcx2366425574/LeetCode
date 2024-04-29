#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 99_M_recoverTree.py
@time: 2023/10/30 22:33
@ide: PyCharm
@desc: 恢复二叉搜索树
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        middle_result = []

        def mid_order(node):

            if node is None:
                return

            mid_order(node.left)
            middle_result.append(node)
            mid_order(node.right)

        mid_order(root)

        left_node = None
        right_node = None
        for i in range(0, len(middle_result)):

            cur = middle_result[i]

            if i == 0:
                if cur.val > middle_result[i + 1].val:
                    right_node = cur
                continue

            if i == len(middle_result) - 1:
                if cur.val < middle_result[i - 1].val:
                    left_node = cur
                continue

            before = middle_result[i - 1]
            after = middle_result[i + 1]
            if before.val < cur.val and after.val < cur.val:
                right_node = cur

            if before.val > cur.val and after.val > cur.val:
                left_node = cur

            # 停止
            if left_node and right_node:
                break

        left_node.val, right_node.val = right_node.val, left_node.val
