#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 2050_H_minimumTime.py
@time: 2023/7/28 23:02
@ide: PyCharm
@desc: 并行课程 III
"""
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        course_relies = defaultdict(set)

        # 初始化
        for relation in relations:
            course_relies[relation[1]].add(relation[0])
            if relation[0] not in course_relies:
                course_relies[relation[0]] = set()

        total_months = 0
        has_learned_courses = set()

        while course_relies:
            tmp_courses = set()
            max_month = 0

            # 完成没有先修课的课程
            for course, relies in course_relies.items():
                if not (relies - has_learned_courses):
                    tmp_courses.add(course)
                    max_month = max(max_month, time[course])

            # 汇总此次修课所需的月份数
            total_months += max_month

            has_learned_courses.update(tmp_courses)

            # 删除已经完成的课程
            for c in tmp_courses:
                course_relies.pop(c)

        return total_months

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        course_relies = [[] for _ in range(n)]
        for x, y in relations:
            course_relies[y - 1].append(x - 1)

        @lru_cache(None)
        def dp(i):

            if not course_relies[i]:
                return time[i]

            return time[i] + max([dp(tmp) for tmp in course_relies[i]])

        return max([dp(i) for i in range(n)])
