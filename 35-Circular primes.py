#!/usr/local/bin/python3
'''
Problem 35 : Circular primes
The number, 197, is called a circular prime
because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
https://projecteuler.net/problem=35
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def is_prime(x, known_primes):
    '''솟수 여부 확인

    솟수이면 True
    솟수가 아니면 False'''

    if x in known_primes:
        return known_primes

    for i in known_primes:
        if x % i == 0:
            return False

    known_primes.append(x)
    known_primes.sort()
    return known_primes


def solution1():
    cp = []
    for i in range(2, 1000000):
        if not is_prime(i):
            continue
        prime = True
        for j in range(1, len(str(i))):
            # print(i, str(i)[j:] + str(i)[:j])
            if not is_prime(int(str(i)[j:] + str(i)[:j])):
                prime = False
        if prime:
            print(i)
            cp.append(i)

    print(len(cp))


def solution():
    cp = []
    primes = []
    for i in range(2, 1000000):
        if not is_prime(i, primes):
            continue
        prime = True
        for j in range(1, len(str(i))):
            # print(i, str(i)[j:] + str(i)[:j])
            if not is_prime(int(str(i)[j:] + str(i)[:j]), primes):
                prime = False
        if prime:
            print(i)
            cp.append(i)

    print(len(cp), sorted(cp))


if __name__ == '__main__':
    solution()

# 55 [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311,
# 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311,
# 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371,
# 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193,
# 939391, 993319, 999331]
