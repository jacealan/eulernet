#!/usr/local/bin/python3
'''
Problem 28 : Number spiral diagonals
Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
https://projecteuler.net/problem=28
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    size = 1001
    matrix = [[0 for i in range(size)] for j in range(size)]
    loc = [0, size - 1]
    cc = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    direction = 0
    for i in range(size * size, 0, -1):
        matrix[loc[0]][loc[1]] = i
        loc_next = [loc[0] + cc[direction][0], loc[1] + cc[direction][1]]
        if -1 in loc_next or size in loc_next:
            direction = (direction + 1) % 4
            loc_next = [loc[0] + cc[direction][0], loc[1] + cc[direction][1]]
        if matrix[loc_next[0]][loc_next[1]]:
            direction = (direction + 1) % 4
            loc_next = [loc[0] + cc[direction][0], loc[1] + cc[direction][1]]
        loc = loc_next

    # for i in range(size):
    #     print(matrix[i])

    sum_diagonal = 0
    for i in range(size):
        if i == size // 2:
            sum_diagonal += matrix[i][i]
        else:
            sum_diagonal += matrix[i][i] + matrix[i][size - i - 1]
    print(sum_diagonal)


if __name__ == '__main__':
    solution()
