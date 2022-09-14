#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 946_validate_stack_sequences.py
@time: 2022/7/15 16:25
@ide: PyCharm
@desc: 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，
只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false。

"""
from copy import copy


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:

        push_list = []
        pop_index = 0

        while pop_index < len(popped):

            if len(push_list) == 0 or push_list[-1] != popped[pop_index]:
                if not pushed:
                    return False
                push_list.append(pushed[0])
                pushed = pushed[1:]
            else:
                pop_index += 1
                push_list.pop()
        return pop_index == len(popped)


if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    s = Solution()
    print(s.validateStackSequences(pushed, popped))
