#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 100_is_same_tree.py
@time: 2022/7/25 17:13
@ide: PyCharm
@desc: 相同的树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def is_same(p_node, q_node):

            if (p_node is None and q_node is not None) or (p_node is not None and q_node is None):
                return False

            if p_node is None and q_node is None:
                return True

            return p_node.val == q_node.val and is_same(p_node.left, q_node.left) and is_same(p_node.right, q_node.right)

        return is_same(p, q)


if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)

    q1 = TreeNode(1)
    q2 = TreeNode(2)
    q3 = TreeNode(3)

    p1.left = p2
    p1.right = p3

    q1.left = q2
    q1.right = p3

    result = Solution().isSameTree(p1, q1)
    print(result)
