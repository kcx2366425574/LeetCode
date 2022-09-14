#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 965_is_unival_tree.py
@time: 2022/7/25 15:55
@ide: PyCharm
@desc: 单值二叉树

如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        value = root.val

        def check(r):
            if r is None:
                return True
            return r.val == value and check(r.left) and check(r.right)
        return check(root)
