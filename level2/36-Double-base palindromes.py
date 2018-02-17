#!/usr/local/bin/python3
'''
Problem 36 : Double-base palindromes
The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.
(Please note that the palindromic number,
in either base, may not include leading zeros.)
https://projecteuler.net/problem=36
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def is_palindrome(x):
    '''대칭수 여부 확인

    대칭수이면 True
    대칭수가 아니면 False'''
    x_str = str(x)
    for i in range((len(x_str) + 1) // 2):  # 수의 맨 앞 숫자부터
        if x_str[i] != x_str[-(i + 1)]:  # 대칭자리 숫자와 비교
            return False
    return True


def solution():
    palidromes = []
    for i in range(1, 1000000):
        num_2 = str(bin(i))[2:]
        if is_palindrome(int(num_2)) and is_palindrome(i):
            palidromes.append(i)
            print(i, bin(i))
    print(sum(palidromes), palidromes)


if __name__ == '__main__':
    solution()
