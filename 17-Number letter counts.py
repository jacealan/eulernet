#!/usr/local/bin/python3
'''
Problem 17 : Number letter counts
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words,
how many letters would be used?
NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
https://projecteuler.net/problem=17
---
프로그래머 Programmer : 제이스 Jace (https://jacealan.github.io)
사용언어 Language : 파이썬 Python 3.6.4
OS : macOS High Sierra 10.13.3
에디터 Editor : Visual Studio Code
'''


def solution():
    num_letters = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                   11: 'eleven', 12: 'twelve', 13: 'thirteen',
                   14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                   17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                   20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                   60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
                   100: 'hundred', 1000: 'thousand', 0: ''}
    num_letters_counts = []

    for i in range(1, 1001):
        num_str = str(i)
        for j in range(len(num_str)):
            # print(len(num_str) - j - 1, num_str[len(num_str) - j - 1:])
            if j == 0:
                num_letter = num_letters[int(num_str[len(num_str) - j - 1])]
            if j == 1:
                if int(num_str[len(num_str) - j - 1]) == 1:
                    num_letter = num_letters[int(
                        num_str[len(num_str) - j - 1:])]
                if int(num_str[len(num_str) - j - 1]) > 1:
                    num_letter = num_letters[int(
                        num_str[len(num_str) - j - 1] + '0')] + num_letter
            if j == 2 and num_str[len(num_str) - j - 1] != '0':
                if num_str[len(num_str) - j:] != '00':
                    num_letter = num_letters[int(
                        num_str[len(num_str) - j - 1])] + num_letters[100] + 'and' + num_letter
                else:
                    num_letter = num_letters[int(
                        num_str[len(num_str) - j - 1])] + num_letters[100]
            if j == 3 and num_str[len(num_str) - j - 1] != '0':
                num_letter = num_letters[int(
                    num_str[len(num_str) - j - 1])] + num_letters[1000] + num_letter
                # if len(num_str) == 1:
                #     num_letter = num_letters[int(num_str)]
        num_letters_counts.append(len(num_letter))
        print(i, num_letter, len(num_letter))

    print(sum(num_letters_counts))


if __name__ == '__main__':
    solution()
