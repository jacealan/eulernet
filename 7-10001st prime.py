#!/usr/local/bin/python3
'''
Problem 7 : 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
https://projecteuler.net/problem=7
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def is_prime(x, known_prime):
    '''솟수 여부 확인

    솟수이면 True
    솟수가 아니면 False'''
    for i in known_prime:
        if x % i == 0:
            return False
    return True


def solution():
    '''10001번째 솟수'''

    primes = [2]
    num = 2
    while len(primes) < 10001:
        if is_prime(num, primes):
            primes.append(num)
            print(len(primes), num)
        num += 1


if __name__ == '__main__':
    solution()
