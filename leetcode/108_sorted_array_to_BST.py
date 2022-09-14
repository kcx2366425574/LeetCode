#!/usr/bin/env python
# encoding: utf-8
"""
@project: 
@author: kuangcx
@contact: 18279911430@163.com
@file: 108_sorted_array_to_BST.py
@time: 2022/8/8 17:15
@ide: PyCharm
@desc: 将有序数组转换为二叉搜索树
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 自己写的递归
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:

        middle = len(nums) // 2
        root = TreeNode(nums[middle])

        def build_tree(left_nums, right_nums, r):
            if not left_nums:
                r.left = None
            else:
                left = len(left_nums) // 2
                left_tree = TreeNode(left_nums[left])
                r.left = left_tree
                build_tree(left_nums[:left], left_nums[left + 1:], left_tree)

            if not right_nums:
                r.right = None
            else:
                right = len(right_nums) // 2
                right_tree = TreeNode(right_nums[right])
                r.right = right_tree
                build_tree(right_nums[:right], right_nums[right + 1:], right_tree)

        build_tree(nums[:middle], nums[middle + 1:], root)
        return root

    # 大佬写的递归
    def sortedArrayToBST1(self, nums: list[int]) -> Optional[TreeNode]:

        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)
