#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 844_backspace_compare.py
@time: 2022/8/23 10:58
@ide: PyCharm
@desc: 比较含退格的字符串

给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

"""
from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspace(target):
            res = deque()
            for ch in target:
                if ch != "#":
                    res.append(ch)
                else:
                    if res:
                        res.pop()
            return "".join(list(res))
        return backspace(s) == backspace(t)
