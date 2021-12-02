from command import Command

f = open("input/day 2 input", "r")

inpu = []
for line in f:
    inpu.append(Command(line))

netFwdDist = 0
netVertDist = 0
for cmd in inpu:
    netFwdDist += cmd.forwardDistance
    netVertDist += cmd.verticalDistance

print(netFwdDist * netVertDist)