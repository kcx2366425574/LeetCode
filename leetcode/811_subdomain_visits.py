#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 811_subdomain_visits.py
@time: 2022/8/1 11:13
@ide: PyCharm
@desc: 子域名访问计数
"""
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        result = defaultdict(int)
        for line in cpdomains:
            count, domains = line.split(" ")
            count = int(count)
            domain_list = domains.split(".")
            for i in range(len(domain_list)):
                result[".".join(domain_list[i:])] += count
        return [f"{count} {domain}" for domain, count in result.items()]
