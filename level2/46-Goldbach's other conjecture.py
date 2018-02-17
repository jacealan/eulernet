#!/usr/local/bin/python3
'''
Problem 46 : Goldbach's other conjecture
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.
9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2
It turns out that the conjecture was false.
What is the smallest odd composite
that cannot be written as the sum of a prime and twice a square?
https://projecteuler.net/problem=46
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def is_prime1(x):
    '''솟수 여부 확인

    솟수이면 True
    솟수가 아니면 False'''
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution1():
    for odd in range(1, 1000000, 2):
        if not is_prime1(odd):

            for j in range(1, odd // 2):
                # print(odd, '=', (odd - 2 * j ** 2), '+ 2 *', j, '** 2')
                break
            else:
                print(odd, 'cannot be written as the sum of a prime and twice a square')


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


def solution():
    primes = [2]
    odd = 1
    while True:
        odd += 2

        if not is_prime(odd, primes):
            for j in range(1, odd):
                if odd - 2 * j ** 2 > 0 and is_prime(odd - 2 * j ** 2, primes):
                    # if odd % 50000 == 1:
                    print(odd, '=', (odd - 2 * j ** 2), '+ 2 *', j, '** 2')
                    break
            else:
                print(odd, 'cannot be written as the sum of a prime and twice a square')
                break
        else:
            primes = is_prime(odd, primes)


if __name__ == '__main__':
    solution()

# pentagons pentagons pentagons 1148 1560090 2167 7042750 -> 5482660
