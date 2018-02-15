#!/usr/local/bin/python3
'''
Problem 31 : Coin sums
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
https://projecteuler.net/problem=31
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    def sumproduct(a_list, b_list):
        # print(a_list, b_list)
        sum = 0
        for a, b in zip(a_list, b_list):
            sum += a * b
        return sum

    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    ways = []
    target = 200

    for count[0] in range(target // coins[0] + 1):
        count[1:] = [0, 0, 0, 0, 0, 0, 0]
        for count[1] in range(target // coins[1] + 1):
            count[2:] = [0, 0, 0, 0, 0, 0]
            if sumproduct(coins, count) > target:
                break
            for count[2] in range(target // coins[2] + 1):
                count[3:] = [0, 0, 0, 0, 0]
                if sumproduct(coins, count) > target:
                    break
                for count[3] in range(target // coins[3] + 1):
                    count[4:] = [0, 0, 0, 0]
                    if sumproduct(coins, count) > target:
                        break
                    for count[4] in range(target // coins[4] + 1):
                        count[5:] = [0, 0, 0]
                        if sumproduct(coins, count) > target:
                            break
                        for count[5] in range(target // coins[5] + 1):
                            count[6:] = [0, 0]
                            if sumproduct(coins, count) > target:
                                break
                            for count[6] in range(target // coins[6] + 1):
                                count[7] = 0
                                if sumproduct(coins, count) > target:
                                    break
                                for count[7] in range(target // coins[7] + 1):
                                    if sumproduct(coins, count) > target:
                                        break
                                    if sumproduct(coins, count) == target:
                                        ways.append(count)
                                        print(count, sumproduct(coins, count))

    print(len(ways))


if __name__ == '__main__':
    solution()
