#!/usr/local/bin/python3
'''
Problem 37 : Truncatable primes
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes
that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
https://projecteuler.net/problem=37
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
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution():
    truncatable_primes = []
    primes = [2, 3, 5, 7]
    ne = ['1', '3', '5', '7', '9']
    for i in range(11, 10000000):
        i_digit = list(str(i))
        if int(i_digit[0]) % 2 == 0 and i_digit[0] != '2':
            continue
        if len(set(i_digit[1:])) > len(set(i_digit[1:]) - {'2', '4', '6', '8'}):
            continue
        # if i % 100000 == 0:
        #     print('...', i)
        if not is_prime(i):
            continue
        primes.append(i)
        num = str(i)
        for j in range(1, len(num)):
            if not is_prime(int(num[j:])) or not is_prime(int(num[:len(num) - j])):
                break
        else:
            truncatable_primes.append(i)
            print('Truncatable primes :', i)

        if len(truncatable_primes) == 11:
            break

    print(sum(truncatable_primes))


if __name__ == '__main__':
    solution()


# Truncatable primes : 23
# Truncatable primes : 37
# Truncatable primes : 53
# Truncatable primes : 73
# Truncatable primes : 313
# Truncatable primes : 317
# Truncatable primes : 373
# Truncatable primes : 797
# Truncatable primes : 3137
# Truncatable primes : 3797
# Truncatable primes : 739397
