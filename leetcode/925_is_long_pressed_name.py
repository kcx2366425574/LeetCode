#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 925_is_long_pressed_name.py
@time: 2022/8/1 17:15
@ide: PyCharm
@desc: 长按键入
"""


class Solution:
    # 虽然可以，但是写的代码太乱了，各种特殊情况都需要单独的代码考虑
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        name_point = 0
        typed_point = 0
        while name_point <= len(name) - 1:
            if name_point != len(name) and typed_point == len(typed):
                return False
            if name[name_point] == typed[typed_point]:
                name_point += 1
                typed_point += 1
            else:
                if name_point > 0 and name[name_point - 1] == typed[typed_point]:
                    typed_point += 1
                else:
                    return False
        for value in typed[typed_point:]:
            if value != name[-1]:
                return False
        return True

    def isLongPressedName1(self, name: str, typed: str) -> bool:
        name_point = 0
        for i in range(len(typed)):
            if name_point < len(name) and name[name_point] == typed[i]:
                name_point += 1
            elif name_point > 0 and typed[i] == name[name_point - 1]:
                continue
            else:
                return False
        return name_point == len(name)


if __name__ == '__main__':
    name = "kikcxmvzi"
    typed = "kiikcxxmmvvzz"
    print(Solution().isLongPressedName(name, typed))
