#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 572_E_is_subtree.py
@time: 2022/9/9 15:42
@ide: PyCharm
@desc: 另一棵树的子树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, one, another):
        if (one is None and another is not None) or (another is None and one is not None):
            return False
        if one is None and another is None:
            return True
        if one.val != another.val:
            return False
        return True and self.compare(one.left, another.left) and self.compare(one.right, another.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and subRoot:
            return False
        sub_result = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if root.val != subRoot.val:
            return sub_result
        else:
            return self.compare(root, subRoot) or sub_result
