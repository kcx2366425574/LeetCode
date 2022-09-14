#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 2114_most_words_found.py
@time: 2022/8/23 10:14
@ide: PyCharm
@desc: 句子中最多的单词数
"""


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max([len(sentence.split(" ")) for sentence in sentences])
