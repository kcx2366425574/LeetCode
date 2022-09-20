#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1048_M_longest_str_chain.py
@time: 2022/9/17 15:17
@ide: PyCharm
@desc: 最长字符串链
"""
from collections import defaultdict, Counter


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=lambda s: len(s))
        str_to_chainlen = Counter()
        max_length = 0
        for w in words:
            for j in range(len(w)):
                curr_w = w[:j] + w[j + 1:]
                str_to_chainlen[w] = max(str_to_chainlen[w], str_to_chainlen[curr_w] + 1)
            max_length = max(max_length, str_to_chainlen[w])
        return max_length


if __name__ == '__main__':
    words = ["a","b","ba","bca","bda","bdca"]
    Solution().longestStrChain(words)
