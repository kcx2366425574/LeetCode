#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 1832_E_checkIfPangram.py
@time: 2022/12/13 0:54
@ide: PyCharm
@desc: 判断句子是否为全字母句
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
