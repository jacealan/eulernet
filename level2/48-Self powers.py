#!/usr/local/bin/python3
'''
Problem 48 : Self powers
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series,
1^1 + 2^2 + 3^3 + ... + 1000^1000.
https://projecteuler.net/problem=48
ref. 3
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    sum = 0
    for i in range(1, 1001):
        sum += i ** i
    print(str(sum)[-10:])


if __name__ == '__main__':
    solution()

# pentagons pentagons pentagons 1148 1560090 2167 7042750 -> 5482660
