#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 897_E_increasingBST.py
@time: 2022/9/16 11:23
@ide: PyCharm
@desc: 递增顺序搜索树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 先中序遍历获取所有节点值，再重新构造一棵新树
    def increasingBST(self, root: TreeNode) -> TreeNode:
        mid_node = []

        def find_node(node):
            if not node:
                return
            find_node(node.left)
            # 把节点的值加进去，不能加入节点，会保留原树的父子结构
            mid_node.append(node.val)
            find_node(node.right)

        find_node(root)
        ret_root = TreeNode(mid_node[0])
        current = ret_root
        for n in mid_node[1:]:
            current.right = TreeNode(n)
            current = current.right
        return ret_root
