#!/usr/local/bin/python3
'''
Problem 43 : Sub-string divisibility
The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:
d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
https://projecteuler.net/problem=43
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
    print(pandigitals[1])
    '''
    if digit == 1:
        return 0, nums, n
    new_nums = []
    for num in nums[:]:
        for i in sorted(list(set(n) - set(num))):
            new_nums.append(num + i)
    return pandigital_list(digit - 1, new_nums, n)


def solution():
    divs = [2, 3, 5, 7, 11, 13, 17]
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pandigitals = pandigital_list(10, n, n)

    substring_divisibility = []
    for num in pandigitals[1]:
        for i in range(2, 9):
            if int(num[i - 1:i + 2]) % divs[i - 2] != 0:
                break
        else:
            print(num, 'is Sub-string divisibility')
            substring_divisibility.append(int(num))

    print(sum(substring_divisibility))


if __name__ == '__main__':
    solution()
