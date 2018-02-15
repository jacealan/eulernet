#!/usr/local/bin/python3
'''
Problem 40 : Champernowne's constant
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part,
find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
https://projecteuler.net/problem=40
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    df = ''
    for i in range(1, 1000000):
        df += str(i)

    print(df[0], df[9], df[99], df[999], df[9999], df[99999], df[999999])
    print(eval('*'.join([df[0], df[9], df[99],
                         df[999], df[9999], df[99999], df[999999]])))


if __name__ == '__main__':
    solution()
