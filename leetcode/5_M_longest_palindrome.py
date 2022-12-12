#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 5_M_longest_palindrome.py
@time: 2022/10/27 20:58
@ide: PyCharm
@desc: 最长回文子串
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest_palindrome = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(longest_palindrome) >= j - i + 1:
                    continue
                tmp = s[i:j + 1]
                if tmp == tmp[::-1]:
                    longest_palindrome = tmp
        return longest_palindrome
