#!/usr/local/bin/python3
'''
Problem 34 : Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers
which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
https://projecteuler.net/problem=34
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def factorial(num):
    '''팩토리알'''
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


def solution():
    for i in range(10):
        if factorial(9) < 10**(i + 1):
            print(factorial(9) * i, 10**(i + 1), i + 1)
            break
    for i in range(100, 1000000):
        digit = str(i)
        sum = 0
        for num in digit:
            sum += factorial(int(num))
            # print(num, end=' ')
        # print(i)
        if sum == i:
            print(i)


if __name__ == '__main__':
    solution()
