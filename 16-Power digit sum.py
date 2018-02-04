#!/usr/local/bin/python3
'''
Problem 16 : Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
https://projecteuler.net/problem=16
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    num = 2 ** 1000
    num_str = str(num)
    nums = []
    for i in num_str:
        nums.append(int(i))
    print(sum(nums), nums)


if __name__ == '__main__':
    solution()
