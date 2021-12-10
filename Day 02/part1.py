input_file = open('input.txt', 'r')
values = [i.split(' ') for i in input_file.readlines()]
input_file.close()

horizontal = 0
depth = 0

for value in values:
    if value[0] == 'forward':
        horizontal += int(value[1])
    elif value[0] == 'down':
        depth += int(value[1])
    elif value[0] == 'up':
        depth -= int(value[1])

print (horizontal * depth)