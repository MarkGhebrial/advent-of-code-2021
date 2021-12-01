f = open("input/day 1 input", "r")

inpu = []
for line in f:
    inpu.append(int(line))

count = 0
lastNum = None
for num in inpu:
    if lastNum != None and lastNum < num:
        count += 1
    lastNum = num

print(count)