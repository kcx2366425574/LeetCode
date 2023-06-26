#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1019_M_nextLargerNodes.py
@time: 2023/4/10 21:46
@ide: PyCharm
@desc: 链表中的下一个更大节点
"""
import copy
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 我还以为是单调栈呢，结果没想清楚，不是
    def nextLargerNodes1(self, head: Optional[ListNode]) -> List[int]:

        # 获取所有的节点值
        node_values = []
        tmp = head
        while tmp:
            node_values.append(tmp.val)
            tmp = tmp.next

        # 通过单调栈
        flag = 0
        result = [0 for i in range(len(node_values))]
        for index in range(len(node_values) - 1, -1, -1):
            if node_values[index] >= flag:
                flag = node_values[index]
            else:
                result[index] = flag

        return result

    # 笑死，怎么还超时了
    def nextLargerNodes2(self, head: Optional[ListNode]) -> List[int]:

        i = head
        j = i.next

        result = []

        while i:
            while j:
                if i and j and i.val < j.val:
                    result.append(j.val)
                    break
                j = j.next
            else:
                result.append(0)

            if i.next:
                i = i.next
                j = i.next
            else:
                break

        return result

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        # 获取所有的节点值
        node_values = []
        tmp = head
        while tmp:
            node_values.append(tmp.val)
            tmp = tmp.next

        stack = [0]
        tmp = copy.deepcopy(stack)

        for value in node_values[::-1]:
            for index in range(len(stack)):
                if value > stack[index]:
                    tmp.pop(0)
                else:
                    tmp = [value].extend(tmp)