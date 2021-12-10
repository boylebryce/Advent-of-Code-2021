input_file = open('input.txt', 'r')
values = [int(line) for line in input_file.readlines()]
input_file.close()

last_window = sum(values[0:2])
increases = 0

for i in range(1, (len(values) - 2)):
    current_window = last_window - values[i - 1] + values[i + 2]
    if current_window > last_window:
        increases += 1
    last_window = current_window

print(increases)