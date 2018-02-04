#!/usr/local/bin/python3
'''
Problem 25 : 1000-digit Fibonacci number
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?
https://projecteuler.net/problem=25
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    fibonacci = [1, 1]
    while len(str(fibonacci[-1])) < 1000:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(len(fibonacci), fibonacci[-1])


if __name__ == '__main__':
    solution()
