#!/usr/local/bin/python3
'''
Problem 39 : Integer right triangles
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
https://projecteuler.net/problem=39
ref. Problem 9
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    num = []
    for p in range(12, 1001):
        triangles = []
        for c in range(p // 3, p // 2):
            for a in range(1, c // 2 + 2):
                b = p - c - a
                # print(a, b, c)
                if b >= c:
                    continue
                if a ** 2 + b ** 2 == c ** 2:
                    triangles.append([a, b, c])
                    # print("피타고라스의 수 :", a, b, c,)
        num.append([p, len(triangles)])
        if len(triangles):
            print(p, len(triangles), triangles)

    num = sorted(num, key=lambda count: count[1])
    print(num)


if __name__ == '__main__':
    solution()
