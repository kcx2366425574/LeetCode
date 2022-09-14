#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 814_prune_tree.py
@time: 2022/7/22 0:52
@ide: PyCharm
@desc: 二叉树剪枝

给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。

返回移除了所有不包含 1 的子树的原二叉树。

节点 node 的子树为 node 本身加上所有 node 的后代。

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

    # 执行用时：32 ms, 在所有 Python3 提交中击败了91.98%的用户
    # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.83%的用户
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        tree_node = deque()

        # 将树节点全部压入栈中
        def search_tree(node):
            if not node:
                return

            tree_node.append(node)
            if node.left:
                search_tree(node.left)
            if node.right:
                search_tree(node.right)

        search_tree(root)
        # 取出所有的节点依次进行判断
        while tree_node:
            node = tree_node.pop()
            if node.left and node.left.val == 0 and node.left.left is None and node.left.right is None:
                node.left = None

            if node.right and node.right.val == 0 and node.right.left is None and node.right.right is None:
                node.right = None

        if root.val == 0 and root.left is None and root.right is None:
            return None
        else:
            return root

    # nb了,直接后序遍历
    def pruneTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root


if __name__ == '__main__':
    # root = [0,null,0,0,0]
    t1 = TreeNode(0)
    t2 = TreeNode(0)
    t3 = TreeNode(0)
    t4 = TreeNode(0)
    t1.right = t2
    t2.left = t3
    t2.right = t4

    s = Solution()
    root = s.pruneTree(t1)
    print(root)