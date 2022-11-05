#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 919_M_CBT_inserter.py
@time: 2022/10/17 17:55
@ide: PyCharm
@desc: 完全二叉树插入器
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.insertable_nodes = self.init_inserter()

    def init_inserter(self):
        queue = deque([self.root])
        insertable_nodes = []
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if not (cur.left and cur.right):
                insertable_nodes.append(cur)
        return insertable_nodes

    def insert(self, val: int) -> int:
        parent = self.insertable_nodes[0]
        current_node = TreeNode(val)
        if not parent.left:
            parent.left = current_node
        else:
            parent.right = current_node
            self.insertable_nodes.pop(0)
        self.insertable_nodes.append(current_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
