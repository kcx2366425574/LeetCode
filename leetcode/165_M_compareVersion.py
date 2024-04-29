#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: 165_M_compareVersion.py
@time: 2023/10/29 19:28
@ide: PyCharm
@desc: 比较版本号
"""
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        version_list_1 = version1.split(".")
        version_list_2 = version2.split(".")

        for version1, version2 in zip_longest(version_list_1, version_list_2, fillvalue=0):
            int_version1 = int(version1)
            int_version2 = int(version2)
            if int_version1 < int_version2:
                return -1
            elif int_version1 > int_version2:
                return 1
        return 0
