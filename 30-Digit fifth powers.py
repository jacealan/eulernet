#!/usr/local/bin/python3
'''
Problem 30 : Digit fifth powers
Surprisingly there are only three numbers
that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written
as the sum of fifth powers of their digits.
https://projecteuler.net/problem=30
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    power = 5
    for i in range(1, 10):
        # print(10**i, 9**power * i)
        if 10**i > 9**power * i:
            break
    limit = 9**power * i

    powers = []
    for i in range(1, limit + 1):
        if i == sum([int(digit)**power for digit in str(i)]):
            powers.append(i)
            print(i)
    print(sum(powers) - 1)


if __name__ == '__main__':
    solution()
