#!/usr/bin/env python3

cubes_dic = {
    'red': 12,
    'green': 13,
    'blue': 14
    }

sum = 0

file = open('day2.input', 'r')
Lines = file.readlines()
for line in Lines:
    possible = True
    game = line.split(':', 1)[0]
    records = line.split(':', 1)[1].split(";")    
    for record in records:
        cubes = record.split(",")
        for cube in cubes:
            cube = cube.lstrip()
            number = int(cube.split(" ")[0])
            color = cube.split(" ")[1].strip()
            if cubes_dic[color] < number:
                possible = False
                break    
        if not possible:
            break
    if possible:
        sum += int(game.split(" ")[1])

print(sum)
