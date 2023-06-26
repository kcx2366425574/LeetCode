#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 804_E_uniqueMorseRepresentations.py
@time: 2023/6/20 22:41
@ide: PyCharm
@desc: 唯一摩尔斯密码词
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        pass_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        pass_set = set()

        for word in words:
            pass_set.add(
                "".join([
                    pass_list[ord(c) - 97] for c in word
                ])
            )

        return len(pass_set)
