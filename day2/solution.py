from toolz import partition

# io
with open('input.txt') as f:
    cmds = f.read().splitlines()

# imperative version
vals = [x.split() for x in cmds]

horizontal_position = 0
depth = 0
aim = 0
for v in vals:
    instruction, mag = v[0], int(v[1])
    if instruction == 'forward':
        horizontal_position += mag
        depth += (aim * mag)
    elif instruction == 'down':
        # depth += mag
        aim += mag
    elif instruction == 'up':
        # depth -= mag
        aim -= mag
    else:
        raise

horizontal_position * depth
