f = open("input/day 1 input", "r")

inpu = []
for line in f:
    inpu.append(int(line))

sums = []
for i in range(len(inpu[:-2])):
    window = inpu[i:i+3]
    sums.append(window[0] + window[1] + window[2])

count = 0
lastNum = None
for num in sums:
    if lastNum != None and lastNum < num:
        count += 1
    lastNum = num

print(count)