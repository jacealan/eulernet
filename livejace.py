#!/usr/local/bin/python3
'''
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    fibonacci = [1, 2]
    while fibonacci[-1] <= 4000000:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(fibonacci)

    wanted = []
    fibonacci.pop()
    for num in fibonacci:
        if num % 2 == 0:
            wanted.append(num)
    print(wanted)

    print(sum(wanted))


if __name__ == '__main__':
    solution()
