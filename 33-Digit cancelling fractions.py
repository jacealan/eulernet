#!/usr/local/bin/python3
'''
Problem 33 : Digit cancelling fractions
The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting to simplify
it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction,
less than one in value,
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
https://projecteuler.net/problem=33
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    aa = 1
    bb = 1
    for i in range(10, 99):
        for j in range(i + 1, 100):
            if '0' is str(j)[1]:
                continue
            b = '0'
            if str(i)[0] is str(j)[0]:
                a = str(i)[1]
                b = str(j)[1]
            if str(i)[0] is str(j)[1]:
                a = str(i)[1]
                b = str(j)[0]
            if str(i)[1] is str(j)[0]:
                a = str(i)[0]
                b = str(j)[1]
            if str(i)[1] is str(j)[1]:
                a = str(i)[0]
                b = str(j)[0]
            if b == '0':
                continue
            # print(i, j, int(a), int(b))
            if i / j == int(a) / int(b):
                print(i, j, int(a), int(b))
                aa *= i
                bb *= j

    for factor in range(aa, 1, -1):
        if aa % factor == 0 and bb % factor == 0:
            print(bb / factor)
            break


if __name__ == '__main__':
    solution()
