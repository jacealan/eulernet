#!/usr/local/bin/python3
'''
Problem 12 : Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
https://projecteuler.net/problem=12
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    num = 1
    triangular = 0
    while True:
        triangular += num  # 삼각수 (1+2+3+...)
        factors = [1, triangular]  # 1과 자신을 인수로
        for i in range(2, triangular):
            if i > triangular / i:
                break
            if triangular % i == 0:  # 인수 찾으면
                factors.append(i)  # 인수로 등록
                if i != triangular // i:  # 짝인수가 있으면
                    factors.append(triangular // i)  # 짝인수 등록
        print(triangular, len(factors))
        num += 1
        if len(factors) > 500:  # 인수가 500개가 넘으면 종료
            break


if __name__ == '__main__':
    solution()
