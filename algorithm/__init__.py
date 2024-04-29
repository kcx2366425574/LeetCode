#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: __init__.py.py
@time: 2022/12/29 22:15
@ide: PyCharm
@desc: 
"""
import paddlenlp
from paddlenlp import Taskflow


similarity = Taskflow("text_similarity")

a = similarity([["世界上什么东西最小", "世界上最小的东西是什么呢?"]])
print(a)
