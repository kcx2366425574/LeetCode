#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 859_buddy_strings.py
@time: 2022/7/26 11:38
@ide: PyCharm
@desc: 亲密字符串

给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回true；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
"""
from collections import Counter


class Solution:

    # 只能交换一次……题目没说清楚
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        count_s = Counter(s)
        count_goal = Counter(goal)

        if s == goal and len(count_goal) == len(goal):
            return False

        for key, count in count_goal.items():
            if count != count_s.get(key, 0):
                return False
        return True

    def buddyStrings1(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if len(set(s)) < len(s) and s == goal:
            return True

        index_list = []
        for index in range(len(s)):
            if s[index] != goal[index]:
                index_list.append(index)

        if len(index_list) != 2:
            return False

        i, j = index_list[0], index_list[1]
        if s[i] == goal[j] and s[j] == goal[i]:
            return True
        return False


if __name__ == '__main__':
    s = "ab"
    goal = "ab"
    print(Solution().buddyStrings(s, goal))
