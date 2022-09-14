#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 757_intersection_size_two.py
@time: 2022/7/23 0:44
@ide: PyCharm
@desc: 设置交集大小至少为2
"""


class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        target_set = set()
        for index in range(len(intervals) - 1, -1, -1):
            start = intervals[index][0]
            end = intervals[index][1]
            intersection = len(target_set & set([i for i in range(start, end + 1, 1)]))
            if intersection >= 2:
                continue
            elif intersection == 1:
                for i in range(start, end + 1, 1):
                    if i not in target_set:
                        target_set.add(i)
                        break
            elif intersection == 0:
                target_set.update({start, start + 1})
        return len(target_set)

    def intersectionSizeTwo1(self, intervals: list[list[int]]) -> int:
        # 参考：https://www.cnblogs.com/grandyang/p/8503476.html
        # 先排序，以右边界为关键字排序，右边界相同的，按左边界降序排序，先处理长度较小的区间
        intervals.sort(key=lambda x: (x[1], -x[0]))
        # print(intervals)

        # 贪心算法，遍历数组。
        # 分三种情况，1二者完全没有交集，2二者有一个数字的交集，3有两个以上的数字交集。
        li = [-1, -1]
        for x in intervals:
            if x[0] <= li[-2]:
                continue
            if x[0] > li[-1]:
                li.append(x[1] - 1)
            li.append(x[1])
            # print(li)

        return len(li) - 2

    def intersectionSizeTwo2(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for k in range(len(vals[i]), m):
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    vals[p].append(j)
                j += 1
        return ans



if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
    count = Solution().intersectionSizeTwo1(intervals)
    print(count)
