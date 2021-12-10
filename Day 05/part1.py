class VentLine:
    def __init__(self, input_line):
        split_input = input_line.split(' -> ')
        self.coord_one = [int(i) for i in split_input[0].split(',')]
        self.coord_two = [int(i) for i in split_input[1].split(',')]

        self.is_vertical = False
        self.is_horizontal = False
        self.is_diagonal = False

        if self.coord_one[0] == self.coord_two[0]:
            self.is_vertical = True
        elif self.coord_one[1] == self.coord_two[1]:
            self.is_horizontal = True
        else:
            self.is_diagonal = True
    
    def to_string(self):
        coord_one_string = str(self.coord_one[0]) + ',' + str(self.coord_one[1]) 
        coord_two_string = str(self.coord_two[0]) + ',' + str(self.coord_two[1])
        direction = ''
        if self.is_vertical:
            direction = 'Vertical'
        elif self.is_horizontal:
            direction = 'Horizontal'
        elif self.is_diagonal:
            direction = 'Diagonal'
        else:
            direction = 'Unknown direction'

        return coord_one_string + ' -> ' + coord_two_string + ' - ' + direction

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

vent_lines = []

for line in input_lines:
    vent_lines.append(VentLine(line))

col_size = max([vent.coord_one[0] for vent in vent_lines] + [vent.coord_two[0] for vent in vent_lines])
row_size = max([vent.coord_one[1] for vent in vent_lines] + [vent.coord_two[1] for vent in vent_lines])
vent_map = []

for i in range(row_size + 1):
    vent_map.append([0] * (col_size + 1))

for vent_line in vent_lines:
    if vent_line.is_vertical:
        col = vent_line.coord_one[0]
        row = min(vent_line.coord_one[1], vent_line.coord_two[1])
        end = max(vent_line.coord_one[1], vent_line.coord_two[1])
        while row <= end:
            vent_map[row][col] += 1
            row += 1
    elif vent_line.is_horizontal:
        row = vent_line.coord_one[1]
        col = min(vent_line.coord_one[0], vent_line.coord_two[0])
        end = max(vent_line.coord_one[0], vent_line.coord_two[0])
        while col <= end:
            vent_map[row][col] += 1
            col += 1
    elif vent_line.is_diagonal:
        

points = 0

for row in vent_map:
    for value in row:
        if value > 1:
            points += 1

print(points)