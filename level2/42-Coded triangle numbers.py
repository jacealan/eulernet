#!/usr/local/bin/python3
'''
Problem 42 : Coded triangle numbers
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to
its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number
then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
https://projecteuler.net/problem=42
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def triangle(n):
    return n * (n + 1) // 2


def solution():
    triangles = [triangle(i) for i in range(1, 21)]
    print(triangles)

    f = open('42-words.txt', 'r', encoding='utf-8')
    words = f.read().replace('"', '').split(',')
    f.close()
    # print(words)

    coded_triangle = []
    for word in words:
        wordvalue = sum([(ord(i) - 64) for i in word])
        if wordvalue in triangles:
            coded_triangle.append(wordvalue)
    print(coded_triangle, len(coded_triangle))


if __name__ == '__main__':
    solution()
