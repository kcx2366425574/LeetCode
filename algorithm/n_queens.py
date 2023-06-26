#!/usr/bin/env python
# encoding: utf-8
"""
@project: leetcode
@author: kuangcx
@contact: 18279911430@163.com
@file: n_queens.py
@time: 2022/12/29 22:15
@ide: PyCharm
@desc: N皇后问题
"""


def is_safe(board, row, column):
    for i in range(0, row):
        if board[i][column] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(column, len(board[0]))):
        if board[x][y] == 1:
            return False
    return True


def print_board(board):
    for nums in board:
        for num in nums:
            print(num, end=' ')
        print()
    print()


def solution(result, board, row):

    if row >= len(board):
        result.append([])
        print_board(board)
        return True

    for y in range(len(board[0])):

        if is_safe(board, row, y):
            board[row][y] = 1
            solution(result, board, row + 1)
            board[row][y] = 0


if __name__ == '__main__':

    n = 8
    init_board = [[0 for i in range(n)] for j in range(n)]
    result = []
    solution(result, init_board, 0)
    print(len(result))
