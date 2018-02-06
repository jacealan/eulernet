#!/usr/local/bin/python3
'''
Problem 27 : Quadratic primes
Euler discovered the remarkable quadratic formula: n^2+n+41
It turns out that the formula will produce 40 primes
for the consecutive integer values 0≤n≤39.
However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,41^2+41+41 is clearly divisible by 41.
The incredible formula n^2−79n+1601 was discovered,
which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n^2+an+b, where |a|<1000 and |b|≤1000
where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
https://projecteuler.net/problem=27
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
        if x % i == 0:
            return False
    return True


def quadratic(n, a, b):
    return n**2 + a * n + b


def solution():
    maxnum = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            primes = []
            while is_prime(quadratic(n, a, b)) and quadratic(n, a, b) > 1:
                primes.append(n)
                n += 1
            if maxnum < len(primes):
                maxnum = len(primes)
                print(a, b, a * b, len(primes), primes)


if __name__ == '__main__':
    solution()
