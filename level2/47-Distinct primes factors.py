#!/usr/local/bin/python3
'''
Problem 47 : Distinct primes factors
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
https://projecteuler.net/problem=47
ref. 3
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def is_prime(x):
    '''솟수 여부 확인

    솟수이면 True
    솟수가 아니면 False'''
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution():
    '''최대소인수 찾기'''

    num_factors = []
    i = 0
    while True:
        i += 1
        num = i
        factors = []  # 소인수 목록
        factor = 2  # 2부터 num의 소인수인지 확인 시작
        while factor <= num:
            if num % factor == 0:  # 소인수이면
                factors.append(factor)  # 소인수 목록에 추가
                num = num / factor  # 1024 -> 512 -> 256 식으로 소인수분해 나누기
            else:
                factor += 1  # 소인수가 아니면 다른 수로 확인
        # print(i, factors)
        num_factors.append(len(set(factors)))
        # if i > 2 and num_factors[-1] == num_factors[-2] == 2:
        #     print('2:', i - 1, i)
        if i > 3 and num_factors[-1] == num_factors[-2] == num_factors[-3] == 3:
            print('3:', i - 2, i - 1, i)
        if i > 4 and num_factors[-1] == num_factors[-2] == num_factors[-3] == num_factors[-4] == 4:
            print('4:', i - 3, i - 2, i - 1, i)
            break


if __name__ == '__main__':
    solution()

# pentagons pentagons pentagons 1148 1560090 2167 7042750 -> 5482660
