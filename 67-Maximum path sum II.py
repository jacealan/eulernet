#!/usr/local/bin/python3
'''
Problem 67 : Maximum path sum II
By starting at the top of the triangle below
and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
   3
  7 4
 2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in 67-triangle.txt
(right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (1012) routes
every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
https://projecteuler.net/problem=67
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    f = open('67-triangle.txt', 'r', encoding='utf-8')
    triangle_str = f.read()
    f.close()
    triangle = [[int(num) for num in nums.split(' ')]
                for nums in triangle_str.split('\n')]
    # print(triangle)

    oldsums = []
    for i, row in enumerate(triangle):
        if i == 0:
            oldsums.append(row)
            continue
        newsums = [[oldsums[0][0] + row[0]]]
        # print(newsums, row[0], oldsums[0][0])
        for j in range(1, len(oldsums)):
            newsums.append([max([num + row[j]
                                 for num in (oldsums[j - 1] + oldsums[j])])])
        newsums.append([oldsums[-1][0] + row[-1]])
        print(newsums)
        oldsums = newsums

    print(max([j for i in newsums for j in i]))


if __name__ == '__main__':
    solution()
