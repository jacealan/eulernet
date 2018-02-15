#!/usr/local/bin/python3
'''
Problem 26 : Reciprocal cycles
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:
1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
https://projecteuler.net/problem=26
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    recur = []
    for divisor in range(2, 1000):
        decimal = '0.'
        num = 10
        nums = []
        while num != 0 and num not in nums:
            nums.append(num)
            decimal += str(num // divisor)
            num = (num % divisor) * 10

            # print(decimal, num, nums)
        if num is not 0:
            recur.append([divisor, len(nums) - nums.index(num)])
            print('1 /', divisor, '=', decimal, len(nums) - nums.index(num))

    recur.sort(key=lambda recurnum: recurnum[1])
    print(recur)


if __name__ == '__main__':
    solution()
