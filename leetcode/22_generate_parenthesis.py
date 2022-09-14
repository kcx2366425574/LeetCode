#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 22_generate_parenthesis.py
@time: 2022/8/5 17:52
@ide: PyCharm
@desc: 括号生成
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []

        def generate(start_str, left, right):
            if left == 0:
                result.append(start_str+")"*right)
                return
            if right == left:
                generate(start_str+"(", left-1, right)
            else:
                generate(start_str+"(", left - 1, right)
                generate(start_str+")", left, right - 1)
        generate("", n, n)
        return result
