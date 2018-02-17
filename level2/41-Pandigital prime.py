#!/usr/local/bin/python3
'''
Problem 41 : Pandigital prime
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
https://projecteuler.net/problem=41
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def is_prime(x):
    '''솟수 여부 확인

    솟수이면 True
    솟수가 아니면 False'''
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def pandigital_list(digit, nums=[], n=['0', '1', '2', '3', '4']):
    '''Pandigital 만들기

    n = ['1', '2', '3', '4']
    pandigitals = pandigital_list(3, n, n)
    print(pandigitals)
    '''
    if digit == 1:
        return 0, nums, n
    new_nums = []
    for num in nums[:]:
        for i in sorted(list(set(n) - set(num))):
            new_nums.append(num + i)
    return pandigital_list(digit - 1, new_nums, n)


def solution():
    n = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(n) - 1, 0, -1):
        pandigitals = pandigital_list(i + 1, n[:i + 1], n[:i + 1])[1]
        print(len(pandigitals), i + 1, n[:i + 1])
        pandigitals.sort()
        pandigitals.reverse()
        for j in pandigitals:
            num = int(j)
            if is_prime(num):
                print(num)
                break


if __name__ == '__main__':
    solution()
