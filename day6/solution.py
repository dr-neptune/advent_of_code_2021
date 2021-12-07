from __future__ import annotations
from dataclasses import dataclass

with open('input.txt') as f:
    fish = [int(i) for i in f.read().split(',')]

@dataclass
class LanternFish:
    life: int
    def decrement(self) -> LanternFish:
        if self.life == 0:
            sea.append(LanternFish(9))
            self.life = 6
        else:
            self.life -= 1
        return self

sea = [LanternFish(i) for i in fish]

# part 1
for i in range(80):
    for j in sea:
        j.decrement()

print(len(sea))

# part 2
fish_dict = {i:0 for i in range(11)}

for f in fish:
    fish_dict[f] += 1

for d in range(256):
    new_swarm = fish_dict[0]
    fish_dict[7] += new_swarm
    fish_dict[9] += new_swarm
    for j in range(10):
        fish_dict[j] = fish_dict[j+1]

print(sum(fish_dict.values()))
