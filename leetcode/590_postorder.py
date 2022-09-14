#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 590_postorder.py
@time: 2022/8/19 0:30
@ide: PyCharm
@desc: N叉树的后序遍历
"""
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    # 递归
    def postorder(self, root: Node) -> list[int]:

        res = []

        def post(r):
            if not r:
                return
            for c in r.children:
                post(c)
            res.append(r.val)

        post(root)
        return res

    # 迭代
    def postorder1(self, root: Node) -> list[int]:

        if not root:
            return []

        child_stack = deque([root])
        res = []
        while child_stack:
            parent = child_stack.popleft()
            for child in parent.children[::-1]:
                if child:
                    child_stack.append(child)
            res = [parent.val].extend(res)
        return res
