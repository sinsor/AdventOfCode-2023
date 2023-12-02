#!/usr/bin/env python3
import re

file1 = open('day1.input', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    list = ''.join(re.findall(r'\d+', line))
    sum += int(list[0] + list[-1])
print(sum)
