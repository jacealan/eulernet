#!/usr/local/bin/python3
'''
Problem 24 : Lexicographic permutations
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
https://projecteuler.net/problem=24
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def recur(numlist, numbers):
    newlist = []
    for i in numlist[:]:
        if len(i) == len(numbers):
            return numlist
        for j in list(set(numbers) - set(i)):
            i.append(j[:])
            newlist.append(i[:])
            # print(i, newlist)
            i.pop()
    return recur(newlist, numbers)


def solution():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numlist = [[num] for num in numbers]
    print(numlist)
    permutation = [int(''.join(num)) for num in recur(numlist, numbers)]
    permutation.sort()
    # print(permutation)
    print(permutation[999999])

    # numlist0 = numbers
    # for i1 in numlist0[:]:
    #     numlist1 = numlist0[:]
    #     numlist1.remove(i1)
    #     # numlist2 = numlist1
    #     for i2 in numlist1[:]:
    #         numlist2 = numlist1[:]
    #         # print(numlist)
    #         numlist2.remove(i2)
    #         # numlist3 = numlist2
    #         for i3 in numlist2[:]:
    #             print(i1, i2, i3)


if __name__ == '__main__':
    solution()
