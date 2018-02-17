#!/usr/local/bin/python3
'''
Problem 49 : Prime permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
https://projecteuler.net/problem=49
ref. 3
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
    n = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    permutations = pandigital_list(4, n, n)
    permutations = digit_list(4, n, n)
    # print(permutations)

    primes = [int(n) for n in permutations[1] if is_prime(int(n))]
    primes.sort()
    # print(primes)

    for i in range(len(primes) - 1):
        for j in range(i + 1, len(primes)):
            if (primes[i] + primes[j]) / 2 in primes:
                first = sorted(list(str(primes[i])))
                second = sorted(list(str((primes[i] + primes[j]) // 2)))
                third = sorted(list(str(primes[j])))
                # print(first, second, third)
                if first == second == third:
                    print(primes[i], (primes[i] + primes[j]) // 2, primes[j])


if __name__ == '__main__':
    solution()


# 중복순열
