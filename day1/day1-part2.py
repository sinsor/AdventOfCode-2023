#!/usr/bin/env python3
import re

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }

sum = 0

file = open('day1.input', 'r')
Lines = file.readlines()
for line in Lines:
    list = re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine', line)
    elm_first = list[0]

    list = re.findall(r'\d+|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])
    elm_last = list[0]

    if elm_first.isdigit():
        first = elm_first[0]
    else:
        first = numbers[elm_first]

    if elm_last.isdigit():
        last = elm_last[0]
    else:
        last = numbers[elm_last[::-1]]

    sum += int(first + last)

print(sum)

