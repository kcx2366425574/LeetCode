#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 145_postorder_traversal.py
@time: 2022/7/19 11:13
@ide: PyCharm
@desc: 二叉树的后序遍历
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ret = []

        def print_value(r):
            if r is None:
                return

            print_value(r.left)
            print_value(r.right)
            ret.append(r.val)
        print_value(root)
        return ret


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t2.left = t3

    s = Solution()
    print(s.postorderTraversal(t1))
