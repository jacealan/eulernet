#!/usr/local/bin/python3
'''
Problem 19 : Counting Sundays
You are given the following information,
but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
https://projecteuler.net/problem=19
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    day_month = [31, 28,  31,  30,  31, 30, 31,  31,  30,  31,  30, 31]
    leap = 0  # 윤년 1
    week = [1]  # 1900년 1월 1일 월요일

    for year in range(1900, 2001):
        days_year = 0
        if year % 4 == 0 and year % 100 != 0:
            leap = 1
        elif year % 400 == 0:
            leap = 1
        else:
            leap = 0
        for month in range(1, 13):
            if month == 2:
                days_month = day_month[month - 1] + leap
            else:
                days_month = day_month[month - 1]
            print(days_month, end=',')
            days_year += days_month
            week.append((week[-1] + days_month) % 7)
        print(':', year, '-', days_year)
        print(week[(year - 1900) * 12:(year - 1900 + 1) * 12])
        # week_of_1.append(week_of_1[-1] + day_year % 7)
    print(week[12:].count(0))


if __name__ == '__main__':
    solution()
