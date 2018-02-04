#!/usr/local/bin/python3
'''
Problem 21 : Amicable numbers
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each of a and b are called
amicable numbers. For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
https://projecteuler.net/problem=21
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    sum_divisors = []
    for num in range(1, 10000):
        divisors = [1]
        for i in range(2, num):
            if i > num // i:
                break
            if num % i == 0:
                if i == num // i:
                    divisors += [i]
                    break
                else:
                    divisors += [i, num // i]
        sum_divisors.append(sum(divisors))
        print(num, sum(divisors), divisors)

    amicable = []
    for i, s in enumerate(sum_divisors[:]):
        if s < 2 or s > len(sum_divisors) - 3 or i + 1 == s:
            continue
        if sum_divisors[s - 1] == i + 1:
            print(i + 1, s)
            amicable.append(s)

    print(sum(amicable), amicable)


if __name__ == '__main__':
    solution()
