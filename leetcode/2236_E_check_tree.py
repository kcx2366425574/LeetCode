#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2236_E_check_tree.py
@time: 2022/10/13 22:53
@ide: PyCharm
@desc: 判断根节点是否等于子节点之和
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val
