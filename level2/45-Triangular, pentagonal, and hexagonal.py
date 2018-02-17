#!/usr/local/bin/python3
'''
Problem 45 : Triangular, pentagonal, and hexagonal
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
https://projecteuler.net/problem=45
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def triangle(n):
    return n * (n + 1) // 2


def pentagon(n):
    return n * (3 * n - 1) // 2


def hexagon(n):
    return n * (2 * n - 1)


def solution():
    limit = 100000
    triangles = set([triangle(i) for i in range(1, limit + 1)])
    pentagons = set([pentagon(i) for i in range(1, limit + 1)])
    hexagons = set([hexagon(i) for i in range(1, limit + 1)])

    print(triangles & pentagons & hexagons)


if __name__ == '__main__':
    solution()

# pentagons pentagons pentagons 1148 1560090 2167 7042750 -> 5482660