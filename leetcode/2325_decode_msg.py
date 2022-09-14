#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@software: pycharm
@file: 2325_decode_msg.py
@time: 2022/7/14 22:17
@ide: PyCharm
@desc: LeetCode自定义的解密规则
"""


class Solution:

    # 暴力两层循环
    def decodeMessage(self, key: str, message: str) -> str:
        char_list = []
        result = ""
        for ch in key:
            if ch not in char_list and ch != " ":
                char_list.append(ch)

        for m in message:
            if m == " ":
                result = f"{result}{m}"
            else:
                result = f"{result}{chr(char_list.index(m) + 97)}"
        return result

    # 本想一次循环替换，但会导致已经替换过的字符被再次替换。
    # 错误
    def decodeMessage1(self, key: str, message: str) -> str:
        char_set = set()
        count = 0
        result = message
        for ch in key:
            if ch != " " and ch not in char_set:
                char_set.add(ch)
                new_char = chr(count + 97)
                result = result.replace(ch, new_char)
                count += 1
        return result

    # 简化暴力循环，并且添加空格映射，不需要额外处理空格逻辑
    def decodeMessage2(self, key: str, message: str) -> str:
        char_dict = {" ": " "}
        count = 0
        for ch in key:
            if ch not in char_dict:
                char_dict[ch] = chr(count + 97)
                count += 1
        return "".join([char_dict[m] for m in message])


if __name__ == '__main__':
    s = Solution()
    key = "the quick brown fox jumps over the lazy dog"
    msg = "vkbs bs t suepuv"
    print(s.decodeMessage(key, msg))
    print(s.decodeMessage2(key, msg))
