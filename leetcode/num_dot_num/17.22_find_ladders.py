#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 17.22_find_ladders.py
@time: 2022/8/6 11:24
@ide: PyCharm
@desc: 单词转换

给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。
"""
from collections import deque, defaultdict


class Solution:
    # 不行
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[str]:
        char_len = len(beginWord)
        used = [0 for i in range(char_len)]
        find_char = [beginWord]
        while find_char:
            char = find_char[-1]
            has_like = False
            if len(set(char) & set(endWord)) == char_len - 1:
                find_char.append(endWord)
                break
            for index, value in enumerate(wordList):
                if not used[index] and len(set(value) & set(char)) == char_len - 1:
                    find_char.append(value)
                    has_like = True
                    used[index] = 1

            if not has_like:
                find_char.pop()
        return find_char

    def findLadders1(self, beginWord: str, endWord: str, wordList: list[str]) -> list[str]:
        # DFS
        hashmap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashmap[word[:i] + '*' + word[i + 1:]].append(word)
        stack = [beginWord]
        w_dict = {beginWord: [beginWord]}
        while stack:
            word = stack.pop()
            if word == endWord:
                return w_dict[word]
            for i in range(len(word)):
                if word[:i] + '*' + word[i + 1:] in hashmap:
                    for tmp in hashmap[word[:i] + '*' + word[i + 1:]]:
                        if tmp not in w_dict:
                            w_dict[tmp] = w_dict[word] + [tmp]
                            stack.append(tmp)
        return []


if __name__ == '__main__':
    begin = "hit"
    end = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]
    print(Solution().findLadders1(begin, end, word_list))
