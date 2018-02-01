#!/usr/local/bin/python3
'''
Problem 6 : Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640. Find the difference
between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
https://projecteuler.net/problem=6
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    '''제곱의 합과 합의 제곱 차이'''

    bound = 100
    sumofsquares = sum([x * x for x in range(1, bound + 1)])
    squaresofsum = sum([x for x in range(1, bound + 1)]) ** 2
    print(squaresofsum - sumofsquares)


if __name__ == '__main__':
    solution()
