#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 19_remove_nth_from_end.py
@time: 2022/8/10 18:02
@ide: PyCharm
@desc: 删除链表的倒数第n个节点
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = head
        slow = head
        count = 0
        while fast.next:
            fast = fast.next
            if count >= n:
                slow = slow.next
            count += 1
        if count < n:
            return slow.next
        else:
            slow.next = slow.next.next
            return head
