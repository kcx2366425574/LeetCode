#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1967_num_of_strings.py
@time: 2022/7/29 15:02
@ide: PyCharm
@desc: 作为子字符串出现在单词中的字符串数目
"""


class Solution:

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count

    # KMP
    def numOfStrings1(self, patterns: list[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            # 生成 pattern 的前缀数组
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
            # 利用前缀数组进行匹配
            j = 0
            for i in range(n):
                while j and word[i] != pattern[j]:
                    j = pi[j - 1]
                if word[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False

        res = 0
        for pattern in patterns:
            res += check(pattern, word)
        return res


if __name__ == '__main__':
    s = "CABAABABAC"
    paterm = "BABAC"
    print(Solution().numOfStrings1([paterm], s))
