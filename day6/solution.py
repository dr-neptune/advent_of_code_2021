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
            return self
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
# that ain't gonna work
