#!/usr/local/bin/python3
'''
Problem 9 : Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
https://projecteuler.net/problem=9
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    '''피타고라스의 수'''

    sumofabc = 1000
    for c in range(sumofabc // 3, sumofabc // 2):
        for a in range(1, c // 2 + 2):
            b = sumofabc - c - a
            # print(a, b, c)
            if b >= c:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                print("피타고라스의 수 :", a, b, c, a * b * c)


if __name__ == '__main__':
    solution()
