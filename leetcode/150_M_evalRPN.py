#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 150_M_evalRPN.py
@time: 2022/10/14 11:05
@ide: PyCharm
@desc: 逆波兰表达式求值
"""
from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque([])
        for char in tokens:
            if char in ("+", "-", "*", "/"):
                second = stack.pop()
                first = stack.pop()
                stack.append(int(eval(f"{first}{char}{second}")))
            else:
                stack.append(char)
        return stack[-1]

