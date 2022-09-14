#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 83_delete_duplicates.py
@time: 2022/8/25 17:04
@ide: PyCharm
@desc: 删除排序链表中的重复数字
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
                continue
            p = p.next
        return head

