#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 01.01_is_unique.py
@time: 2022/9/8 11:25
@ide: PyCharm
@desc: 判断字符是否唯一
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)
