#!/usr/local/bin/python3
'''
Problem 4 : Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
https://projecteuler.net/problem=4
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
    '''대칭수 찾기'''

    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):  # 3자리수 * 3자리수 중 대칭 수 찾기
                palindromes.append(i * j)  # 대칭수 목록 만들기
    palindromes.sort()  # 대칭수 크기순으로 정렬
    print(palindromes)
    print(palindromes[-1])  # 가장 큰 대칭 수 출력


if __name__ == '__main__':
    solution()
