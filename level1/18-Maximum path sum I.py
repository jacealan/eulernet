#!/usr/local/bin/python3
'''
Problem 18 : Maximum path sum I
By starting at the top of the triangle below
and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
   3
  7 4
 2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes,
it is possible to solve this problem by trying every route.However, Problem 67,
is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
https://projecteuler.net/problem=18
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    triangle_str = '''75
                95 64
                17 47 82
                18 35 87 10
                20 04 82 47 65
                19 01 23 75 03 34
                88 02 77 73 07 63 67
                99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
                41 48 72 33 47 32 37 16 94 29
                53 71 44 65 25 43 91 52 97 51 14
                70 11 33 28 77 73 17 78 39 68 17 57
                91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
                04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
    triangle = [[int(num) for num in nums.strip().split(' ')]
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
            newsums.append([num + row[j]
                            for num in (oldsums[j - 1] + oldsums[j])])
        newsums.append([oldsums[-1][0] + row[-1]])
        print(newsums)
        oldsums = newsums

    print(max([j for i in newsums for j in i]))


if __name__ == '__main__':
    solution()
