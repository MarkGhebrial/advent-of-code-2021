from command import Command

f = open("input/day 2 input", "r")

inpu = []
for line in f:
    inpu.append(Command(line))

aim = 0
depth = 0
horizDist = 0
for cmd in inpu:
    aim += cmd.verticalDistance
    depth += aim * cmd.forwardDistance
    horizDist += cmd.forwardDistance

print(horizDist * depth)