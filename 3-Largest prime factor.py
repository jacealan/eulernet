#!/usr/local/bin/python3
'''
Problem 3 : Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
https://projecteuler.net/problem=3
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
    for i in range(2, x):
        if x % i != 0:
            return False
    return True


def solution():
    '''최대소인수 찾기'''

    num = 1024  # 문제의 수
    factors = []  # 소인수 목록
    factor = 2  # 2부터 num의 소인수인지 확인 시작
    while factor <= num:
        if num % factor == 0:  # 소인수이면
            factors.append(factor)  # 소인수 목록에 추가
            num = num / factor  # 1024 -> 512 -> 256 식으로 소인수분해 나누기
        else:
            factor += 1  # 소인수가 아니면 다른 수로 확인
    print(factors)


if __name__ == '__main__':
    solution()
