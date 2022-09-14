#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 731_my_calendar_two.py
@time: 2022/7/19 0:29
@ide: PyCharm
@desc: 我的日程安排表II
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。

每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。

请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
"""
import bisect
from collections import defaultdict


# 超出时间限制
# 太sd了
class MyCalendarTwo:

    def __init__(self):
        self.calendar = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        result = True
        for i in range(start, end, 1):
            if self.calendar.get(i, 0) == 2:
                result = False
        if result:
            for i in range(start, end, 1):
                self.calendar[i] += 1
        return result


# 维护两个列表，一个记录日历安排，另一个记录两个安排冲突的时间段
class MyCalendarTwo1:

    def __init__(self):
        self.books = []
        self.overs = []

    def book(self, start: int, end: int) -> bool:
        for over_start, over_end in self.overs:
            if over_start <= end and over_end <= start:
                return False
        self.books.append((start, end))
        for book_start, book_end in self.books:
            s = max(start, book_start)
            e = min(end, book_end)
            if s < e:
                self.overs.append((s, e))
        return True
