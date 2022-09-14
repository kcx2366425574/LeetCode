#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 476_find_complement.py
@time: 2022/7/30 15:24
@ide: PyCharm
@desc: 数字的补数
"""


class Solution:
    def findComplement(self, num: int) -> int:

        char_list = ["0", "b"]
        bin_num = bin(num)[2:]
        for ch in bin_num:
            if ch == "0":
                char_list.append("1")
            else:
                char_list.append("0")
        num_str = "".join(char_list)
        return int(num_str, 2)


if __name__ == '__main__':
    num = 5
    print(Solution().findComplement(num))
