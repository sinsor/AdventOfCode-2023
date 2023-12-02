#!/usr/bin/env python3

sum = 0

file = open('day2.input', 'r')
Lines = file.readlines()
for line in Lines:
    cubes_dic = {'red': 0, 'green': 0, 'blue': 0}
    records = line.split(':', 1)[1].split(";")    
    for record in records:        
        cubes = record.split(",")
        for cube in cubes:
            cube = cube.lstrip()
            number = int(cube.split(" ")[0])
            color = cube.split(" ")[1].strip()
            if number > cubes_dic[color]:
                cubes_dic[color] = number

    sum += int(cubes_dic['red']) * int(cubes_dic['green']) * int(cubes_dic['blue'])

print(sum)
