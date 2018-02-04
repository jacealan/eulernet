#!/usr/local/bin/python3
'''
Problem 14 : Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
https://projecteuler.net/problem=14
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    max_length = 0
    for i in range(2, 1000000):
        n = i
        collatz = [n]
        while n != 1:
            if n % 2 == 0:  # 짝수면
                n = n // 2
            else:  # 홀수면
                n = n * 3 + 1
            collatz.append(n)
        if max_length < len(collatz):  # 가장 긴 Collatz sequence는
            max_length = len(collatz)
            print(i, len(collatz))


if __name__ == '__main__':
    solution()
