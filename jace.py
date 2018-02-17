#!/usr/local/bin/python3
'''
프로그래머 Programmer : 제이스 Jace
>>> https://jacealan.github.io
>>> https://github.com/jacealan/eulernet.git
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
Ref.
>>> https://projecteuler.net/about
>>> http://euler.synap.co.kr
'''


def is_prime(x):
    '''솟수 여부 확인

    솟수이면 True
    솟수가 아니면 False'''
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def factorial(num):
    '''팩토리알'''
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


def divisors(num):
    '''약수'''
    nums = [1, num]
    for i in range(2, num):
        if i > num // i:
            break
        if num % i == 0:
            if i == num // i:
                nums += [i]
                break
            else:
                nums += [i, num // i]
    return sorted(nums)


def is_palindrome(x):
    '''대칭수 여부 확인

    대칭수이면 True
    대칭수가 아니면 False'''
    x_str = str(x)
    for i in range((len(x_str) + 1) // 2):  # 수의 맨 앞 숫자부터
        if x_str[i] != x_str[-(i + 1)]:  # 대칭자리 숫자와 비교
            return False
    return True


def digit_list(digit, nums=[], n=['0', '1', '2', '3', '4']):
    '''자리수 만들기

    n = ['1', '2', '3', '4']
    digits = digit_list(3, n, n)
    print(digits[1])
    '''
    if digit == 1:
        # print(nums)
        return 0, nums, n
    new_nums = []
    for num in nums[:]:
        for i in n:
            new_nums.append(num + i)
            # print(new_nums)

    return digit_list(digit - 1, new_nums, n)


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
    pass


if __name__ == '__main__':
    solution()
