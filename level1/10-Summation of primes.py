#!/usr/local/bin/python3
'''
Problem 10 : Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
https://projecteuler.net/problem=10
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
    if x == 2:
        return True
    for i in known_prime:
        if x % i == 0:
            return False
    return True


def solution1():
    '''솟수의 합'''

    limit = 2000000
    primes = []
    for num in range(2, limit + 1):
        if num in primes:
            continue
        if is_prime(num, primes):
            primes.append(num)
    print(sum(primes))


def solution2():
    '''솟수의 합'''

    limit = 100000
    numbers = list(range(2, limit + 1))
    primes = []
    num = numbers[0]
    while True:
        if is_prime(num, primes):
            for i in numbers[:]:
                if i % num == 0:
                    numbers.remove(i)
            primes.append(num)
            # print(sum(primes), primes)
        print(len(numbers))

        if len(numbers) == 0:
            break
        num = numbers[0]
    print(sum(primes))


def solution3():
    '''솟수의 합'''

    limit = 100000
    nums = list(range(2, limit + 1))
    primes = []
    num = nums[0]
    while num < limit + 1:
        if is_prime(num, primes):
            nums = sorted(
                list(set(nums) - set(list(range(num, limit + 1, num)))))
            primes.append(num)
            # print(nums)
        if len(nums) == 0:
            break
        num = nums[0]
        # print()
    print(sum(primes))


if __name__ == '__main__':
    solution1()
    # solution2()
    # solution3()
