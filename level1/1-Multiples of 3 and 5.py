#!/usr/local/bin/python3
'''
Problem 1 : Multiples of 3 and 5
If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution1():
    '''1000미만의 3배수 또는 5의 배수의 합

    3이 배수는 3으로 나눈 나머지가 0
    5의 배수는 5로 나눈 나머지가 0'''

    multiples = []
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            print(i, end=',')  # 3또는 5의 배수 출력
            multiples.append(i)
    print(multiples)
    print('답은', sum(multiples))


def solution2():
    '''list comprehension 이용'''

    print(sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]))


if __name__ == '__main__':
    solution1()
    solution2()
