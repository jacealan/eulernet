#!/usr/local/bin/python3
'''
Problem 23 : Non-abundant sums
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.
A number n is called deficient
if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written
as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number
that cannot be expressed
as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
https://projecteuler.net/problem=23
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def divisors(num):
    nums = [1, num]
    for i in range(2, num):
        if i > num // i:
            break
        if num % i == 0:
            if i == num // i:
                nums += [i]
                break
            else:
                nums += [i, num // i]
    return sorted(nums)


def solution():
    abundants = []
    for i in range(2, 28123):
        # print(divisors(i)[:-1])
        # if sum(divisors(i)[:-1]) == i:
        #     print(i, divisors(i)[:-1], 'perfect number')
        # if sum(divisors(i)[:-1]) < i:
        #     print(i, divisors(i)[:-1], 'deficient number')
        if sum(divisors(i)[:-1]) > i:
            # print(i, divisors(i)[:-1], 'abundant number')
            abundants.append(i)
    # print(abundants)

    sumabundants = []
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            sumabundants.append(abundants[i] + abundants[j])

    nums = set(list(range(1, 28124)))
    # print(nums)
    print(sum(list(nums - set(sumabundants))))


if __name__ == '__main__':
    solution()
