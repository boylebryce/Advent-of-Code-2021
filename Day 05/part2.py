class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Line:
    def __init__(self, first, second):
        self.coords = []
        x = first.x
        y = first.y

        # Start at first, increment up to one before second
        while x != second.x or y != second.y:
            self.coords.append(Coord(x, y))

            if x < second.x:
                x += 1
            elif x > second.x:
                x += -1

            if y < second.y:
                y += 1
            elif y > second.y:
                y += -1
                
        # Append second that wasn't reached with increments
        self.coords.append(second)

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

lines = []
vents = []
size = 0
points = 0

for line in input_lines:
    
    split_inputs = [pair.strip().split(',') for pair in line.split(' -> ')]
    coords = []

    for pair in split_inputs:
        for value in pair:
            coords.append(int(value))

    size = max(coords) if max(coords) > size else size
    first = Coord(coords[0], coords[1])
    second = Coord(coords[2], coords[3])
    lines.append(Line(first, second))

for i in range(size + 1):
    vents.append([0] * (size + 1))

for line in lines:
    for coord in line.coords:
        vents[coord.x][coord.y] += 1

for line in vents:
    for value in line:
        if value > 1:
            points += 1

print(points)