#!/usr/local/bin/python3
'''
Problem 38 : Pandigital multiples
Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
https://projecteuler.net/problem=38
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    for i in range(1, 10000):
        multiple = ''
        for j in range(1, 10):
            multiple += str(i * j)
            if len(multiple) > 9 or '0' in multiple:
                break
            if len(multiple) == 9 and len(set(multiple)) == len(multiple):
                print(i, j, multiple)
                break


if __name__ == '__main__':
    solution()
