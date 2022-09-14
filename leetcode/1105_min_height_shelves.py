#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 1105_min_height_shelves.py
@time: 2022/8/3 14:19
@ide: PyCharm
@desc: 填充书架
"""


class Solution:
    #
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        min_height = [1000000 for _ in range(len(books) + 1)]
        min_height[0] = 0
        for i in range(1, len(books)+1):
            first_book = i
            height = books[i][1]
            total_width = books[i][0]
            while total_width < shelfWidth:
                if total_width + books[first_book-1][0] <= shelfWidth and first_book > 0:
                    total_width += books[first_book-1][0]
                    height = max(books[first_book-1][1], height)
                    first_book -= 1
                else:
                    break

            min_height[i] = min(min_height[first_book-1] + height, min_height[i])
        return min_height[-1]

    def minHeightShelves1(self, books: list[list[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [1000000] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            tmp_width, j, h = 0, i, 0
            while j > 0:
                tmp_width += books[j - 1][0]
                if tmp_width > shelf_width:
                    break
                h = max(h, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + h)
                j -= 1
        return dp[-1]


if __name__ == '__main__':
    books = [[1,3],[2,4],[3,2]]
    width = 6
    print(Solution().minHeightShelves(books, width))
