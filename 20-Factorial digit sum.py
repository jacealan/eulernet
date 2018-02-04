#!/usr/local/bin/python3
'''
Problem 20 : Factorial digit sum
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
https://projecteuler.net/problem=20
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


def solution():
    digit = [int(n) for n in str(factorial(100))]
    print(sum(digit), digit)


if __name__ == '__main__':
    solution()
