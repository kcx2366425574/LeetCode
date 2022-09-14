#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 876_middle_node.py
@time: 2022/7/29 15:21
@ide: PyCharm
@desc: 链表的中间结点

给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 将所有节点加入数组中，返回中间元素
    def middleNode(self, head: ListNode) -> ListNode:
        node_list = []
        p = head
        while p:
            node_list.append(p)
            p = p.next
        return node_list[len(node_list) // 2]

    # 时间换空间，两次循环
    # 第一次确定链表长度N，第二次遍历N//2次
    def middleNode1(self, head: ListNode) -> ListNode:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        p = head
        for i in range(length // 2):
            p = p.next
        return p

    # 快慢指针
    # 快指针每次遍历取下一个节点，慢指针每两次遍历取下一个节点
    def middleNode2(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
