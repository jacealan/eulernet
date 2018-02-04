#!/usr/local/bin/python3
'''
Problem 15 : Lattice paths
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
https://projecteuler.net/problem=15
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


def solution1():
    '''모든 길 찾기

    가로로 끝까지, 세로로 끝까지 가는 길을 시작으로
    찾은 길을 돌아가서 다른 길을 찾는 방식'''
    toright = 5
    todown = 5
    path = [1 for i in range(toright)] + [0 for i in range(todown)]
    location = toright + todown - 1
    paths = []
    paths.append(path[:])
    while True:
        if path[location] == 0:
            location -= 1
            if location < 0:
                break
        else:
            if path[0:location].count(0) < todown:
                path[location] = 0
                for i in range(location + 1, len(path)):
                    if path[0:i].count(1) < toright:
                        path[i] = 1
                    elif path[0:i].count(0) < todown:
                        path[i] = 0
                    else:
                        path[i] = 1
                paths.append(path[:])
                # print(len(paths), paths)
                location = toright + todown - 1
            else:
                location -= 1

            # input()

    print(len(paths))


def solution2():
    '''중복 조합으로 격자길 찾기'''
    toright = 5
    todown = 5
    print(factorial(toright + todown) //
          factorial(toright) // factorial(todown))


if __name__ == '__main__':
    solution1()
    solution2()
