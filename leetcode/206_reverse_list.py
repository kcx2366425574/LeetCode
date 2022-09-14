#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 206_reverse_list.py
@time: 2022/8/10 15:26
@ide: PyCharm
@desc: 反转列表
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 两次循环，太傻了
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        p = head
        while p:
            node_list.append(p)
            p = p.next

        t = None
        for value in node_list:
            value.next = t
            t = value
        return t

    # nb一次循环
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = None
        y = head
        while y:
            tmp = y.next
            y.next = x
            x = y
            y = tmp
        return x
