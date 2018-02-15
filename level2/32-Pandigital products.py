#!/usr/local/bin/python3
'''
Problem 32 : Pandigital products
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
https://projecteuler.net/problem=32
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    nums_list = []
    nums_full = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    nums = nums_full
    for d1 in nums[:]:
        nums.remove(d1)
        for d2 in nums[:]:
            nums.remove(d2)
            for d3 in nums[:]:
                nums.remove(d3)
                for d4 in nums[:]:
                    nums.remove(d4)
                    for d5 in nums[:]:
                        nums.remove(d5)
                        for d6 in nums[:]:
                            nums.remove(d6)
                            for d7 in nums[:]:
                                nums.remove(d7)
                                for d8 in nums[:]:
                                    nums.remove(d8)
                                    for d9 in nums[:]:
                                        nums_list.append(
                                            [d1, d2, d3, d4, d5, d6, d7, d8, d9])
                                    nums.append(d8)
                                nums.append(d7)
                            nums.append(d6)
                        nums.append(d5)
                    nums.append(d4)
                nums.append(d3)
            nums.append(d2)
        nums.append(d1)

    # print(nums_list)
    cs = []

    for nums in nums_list:
        for i in range(1, len(nums_full[:]) - 1):
            for j in range(i + 1, len(nums_full[:])):
                a = int(''.join(nums[0:i]))
                b = int(''.join(nums[i:j]))
                c = int(''.join(nums[j:]))
                if a * b == c:
                    print(a, '*', b, '=', c)
                    cs.append(c)
    print(sum(list(set(cs))))


if __name__ == '__main__':
    solution()
