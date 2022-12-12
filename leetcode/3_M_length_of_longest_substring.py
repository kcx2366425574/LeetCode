#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 3_M_length_of_longest_substring.py
@time: 2022/10/27 15:50
@ide: PyCharm
@desc: 无重复字符的最长子串
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_dict = {}

        max_len = 0
        start = 0
        end = 0

        for index, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = index
                end = index
            else:
                max_len = max(max_len, end - start + 1)
                start = char_dict[char] + 1
                end = start
                char_dict = {key: value for key, value in char_dict.items() if value >= start}
                char_dict[char] = index
        return max(max_len, end - start + 1)
