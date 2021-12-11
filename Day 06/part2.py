import collections
from typing import Collection

class Fish:
    def __init__(self, start, days):
        self.start = start
        self.days = days

input_fishes = '3,5,1,2,5,4,1,5,1,2,5,5,1,3,1,5,1,3,2,1,5,1,1,1,2,3,1,3,1,2,1,1,5,1,5,4,5,5,3,3,1,5,1,1,5,5,1,3,5,5,3,2,2,4,1,5,3,4,2,5,4,1,2,2,5,1,1,2,4,4,1,3,1,3,1,1,2,2,1,1,5,1,1,4,4,5,5,1,2,1,4,1,1,4,4,3,4,2,2,3,3,2,1,3,3,2,1,1,1,2,1,4,2,2,1,5,5,3,4,5,5,2,5,2,2,5,3,3,1,2,4,2,1,5,1,1,2,3,5,5,1,1,5,5,1,4,5,3,5,2,3,2,4,3,1,4,2,5,1,3,2,1,1,3,4,2,1,1,1,1,2,1,4,3,1,3,1,2,4,1,2,4,3,2,3,5,5,3,3,1,2,3,4,5,2,4,5,1,1,1,4,5,3,5,3,5,1,1,5,1,5,3,1,2,3,4,1,1,4,1,2,4,1,5,4,1,5,4,2,1,5,2,1,3,5,5,4,5,5,1,1,4,1,2,3,5,3,3,1,1,1,4,3,1,1,4,1,5,3,5,1,4,2,5,1,1,4,4,4,2,5,1,2,5,2,1,3,1,5,1,2,1,1,5,2,4,2,1,3,5,5,4,1,1,1,5,5,2,1,1'
fishes = [int(fish) for fish in input_fishes.split(',')]

days = 256
spawn_timer = 8
reset_timer = 6
fish_list = [0] * (spawn_timer + 1)

for fish in fishes:
    fish_list[fish] += 1

for day in range(days):
    print(f'Day {day}, fish list {fish_list}')

    spawns = fish_list[0]
    respawns = fish_list[0]

    fish_deque = collections.deque(fish_list)
    fish_deque.rotate(-1)
    fish_list = list(fish_deque)

    fish_list[reset_timer] += respawns
    fish_list[-1] = spawns

print(sum(fish_list))