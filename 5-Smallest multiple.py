#!/usr/local/bin/python3
'''
Problem 5 : Smallest multiple
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
https://projecteuler.net/problem=5
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution1():
    '''최소공배수 찾기'''

    bound = 10
    product = 1  # 수들의 곱, 최대공배수(?)
    for i in range(1, bound + 1):
        product *= i

    for i in range(bound + 1, product):
        for j in range(1, bound + 1):
            if i % j != 0:  # 공배수 확인
                break
        else:
            print(i)  # 최소공배수 출력
            break


def solution2():
    '''최소공배수 찾기

    1,2의 최소공배수 찾기
    1,2의 최소공배수와 3의 최소공배수 찾기 : 1,2,3의 최소공배수
    1,2,3의 최소공배수와 4의 최소공배수 찾기 : 1,2,3,4의 최소공배수
    1,2,3,4의 최소공배수와 5의 최소공배수 찾기 : 1,2,3,4,5의 최소공배수
    ...
    1~19의 최소공배수와 20의 최소공배수 찾기'''

    bound = 20
    i = 2
    multiple = 1
    count = 1
    while True:
        if multiple * count % i == 0:  # 최소공배수의 배수 중 수의 공배수찾기
            multiple = multiple * count
            print(multiple, ': 1 ~', i)
            i += 1
            count = 1
            if i > bound:
                break
        else:  # 최소공배수의 배수들
            # print(multiple * count, i)
            count += 1
    print(multiple)


if __name__ == '__main__':
    # solution1()
    solution2()
