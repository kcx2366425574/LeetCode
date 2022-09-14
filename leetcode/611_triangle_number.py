#!/usr/bin/env python
# encoding: utf-8
"""
@project: all_my_known_python
@author: kuangcx
@contact: 18279911430@163.com
@file: 611_triangle_number.py
@time: 2022/7/24 21:18
@ide: PyCharm
@desc: 有效三角形
"""


class Solution:

    # 暴力解法，三层遍历，超时
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1, 1):
                for k in range(j + 1, len(nums), 1):
                    print(nums[i], nums[j], nums[k])
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
                    else:
                        break
        return count

    # 双层遍历 + 二分
    # 好慢……超过5%
    def triangleNumber1(self, nums: list[int]) -> int:
        nums.sort()

        def find_index(first, second, start, end):
            if first + second <= nums[start]:
                return None
            if first + second > nums[end]:
                return end
            middle = (start + end) // 2
            if nums[middle] < first + second <= nums[middle + 1]:
                return middle
            if first + second > nums[middle]:
                return find_index(first, second, middle, end)
            else:
                return find_index(first, second, start, middle)
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1, 1):
                index = find_index(nums[i], nums[j], j + 1, len(nums)-1)
                if index:
                    count += index - j
        return count

    # 别人家的双层遍历＋二分查找
    def triangleNumber2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        return ans

    # 双指针
    def triangleNumber3(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k - j, 0)
        return ans


if __name__ == '__main__':
    nums = [48,66,61,46,94,75]
    data = Solution().triangleNumber1(nums)
    print(data)
