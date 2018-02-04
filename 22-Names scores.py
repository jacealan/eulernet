#!/usr/local/bin/python3
'''
Problem 22 : Names scores
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position
in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
https://projecteuler.net/problem=22
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    f = open('22-names.txt', 'r', encoding='utf-8')
    names = f.read().replace('"', '').split(',')
    f.close()

    names.sort()
    name_score = []
    for i, name in enumerate(names):
        print(sum([(ord(i) - 64) for i in name]), (i + 1))
        name_score.append(sum([(ord(i) - 64) for i in name]) * (i + 1))  # A=65

    print(sum(name_score))


if __name__ == '__main__':
    solution()
